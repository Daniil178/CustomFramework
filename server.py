import sys
import signal
import argparse
import socket
import threading
from queue import Queue

def stop_server(*argc, **argv):
    """Catch SIGINT signal from keyboard and exit from programm
    """
    print("\nServer stoping...")
    sys.exit(0)

def worker(que):
    while True:
        conn = que.get()
        if conn is None:
            que.put(conn)
        else:
            with conn:
                data = conn.recv(1024)
                answer = data.decode()  # Change to path function
                print(f"{answer}")
                try:
                    conn.sendall(answer.encode())
                except socket.error:
                    print(f"Error: cannot send data to {conn}")
                else:
                    print(f"Success: client answer in {threading.current_thread().name}")

class ServerThreadMain(threading.Thread):
    def __init__(self, workers_num, host, port):
        super().__init__(daemon=True)
        self.stats = {}
        self.conn_que = Queue(maxsize=100)
        self.host = host
        self.port = port
        self.workers = workers_num

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((self.host, self.port))
            sock.listen(100)
            self.workers = [
                threading.Thread(
                    target=worker,
                    name=f"worker-{i}",
                    args=(self.conn_que,),
                    daemon=True,
                )
                for i in range(self.workers)
            ]
            for thread in self.workers:
                thread.start()

            while True:
                conn, addr = sock.accept()
                self.conn_que.put(conn)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, stop_server)
    parser = argparse.ArgumentParser(
        description='master-worker server for hadling clients requests')
    parser.add_argument('host', type=str,
                    help='host')
    parser.add_argument('port', type=int,
                    help='port')
    parser.add_argument('-w', '--workers', type=int, default=10,
                        help='Number of threads')
    args = parser.parse_args()

    server = ServerThreadMain(args.workers, args.host, args.port)
    server.start()
    print("Server started!")
    server.join()