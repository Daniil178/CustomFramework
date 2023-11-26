import ujson
import requests
import re
#"/search/cwe-257/?type=json&abc=zxc"
#CWE-257
#detail=False, methods=['get', url_path=r'search/(?P<cwe_start>[a-zA-Z0-9\-+')  "[a-z]{3}-[0-9]{3}"
class Request(object):
    def __init__(self, method, url_path ):
        self.method = method.upper()
        self.get_args = (url_path[url_path.index("?"): -1])[1:-1] if url_path.index("?") != -1 else None
        param_temp = url_path[0:url_path.index("?") - 1]
        self.param = param_temp[param_temp.rindex("/")+1:-1] if self.get_args else url_path[url_path.rindex("/"):-1]
        self.path = url_path





    def __call__(self, f):
        def wrapper(obj, *args, **kwargs):
            payload = f(obj, *args, **kwargs)
            print(f"PAYLOAD {payload}")
            data = {}
            for arg in self.get_args.split("&"):
                data[arg.split("=")[0]] = arg.split("=")[1]
            args = {
                'method': self.method,
                'url': 'http://{}/{}'.format(obj.host, self.path)
            }
            if payload is not None:
                args['data'] = data
            return requests.request(**args)
        return wrapper

class GetRequest(Request):
    def __init__(self, path, h=None):
        if h is None:
            super().__init__("GET", path)
        else:
            super().__init__("GET", path, h)

class PostRequest(Request):
    def __init__(self, path, h=None):
        if h is None:
            super().__init__("POST", path)
        else:
            super().__init__("POST", path, h)

class PutRequest(Request):
    def __init__(self, path, h=None):
        if h is None:
            super().__init__("PUT", path)
        else:
            super().__init__("PUT", path, h)

class DeleteRequest(Request):
    def __init__(self, path, h=None):
        if h is None:
            super().__init__("DELETE", path)
        else:
            super().__init__("DELETE", path, h)

myToken = 'Secret_key_1234567890'

class DecoRequests(object):
    def __init__(self, host):
        self.host = host

    @GetRequest(path="userlist", h={'access_token':myToken})
    def list_employees(self):
        pass

    @GetRequest(path="users", h={'access_token':myToken})
    def list_employee(self, username):
        return {"username":username}

    @PostRequest(path="users", h={'access_token':myToken})
    def add_employee(self, employee_data):
        return employee_data

    @PutRequest(path="users", h={'access_token':myToken})
    def update_employee(self, employee_data):
        return employee_data

    @DeleteRequest(path="users", h={'access_token':myToken})
    def rm_employee(self, username):
        return {"username":username}