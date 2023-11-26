import re

class Request(object):
    def __init__(self, method, url_path):
        self.method = method.upper()
        self.get_args = url_path.index("?")(url_path[url_path.index("?"): -1])[1:-1] if url_path.find("?") != -1 else None
        param_temp = url_path[0:url_path.index("?") - 2] if url_path.find("?") != -1 else url_path[:]
        param_index = param_temp.rfind('(#')
        if param_index != -1:
            self.param = param_temp[param_index + 2:]
            self.path = param_temp[:-2]
        else:
            self.param = None
        self.path = url_path
        print(f"DECO INIT {self.path, method, url_path}")

    def __call__(self, f):
        def wrapper(request, response,  *args, **kwargs):
            data = {}
            for arg in self.get_args.split("&"):
                data[arg.split("=")[0]] = arg.split("=")[1]
            response_data = f(request, *args, **kwargs)
            if response_data is not None:
                response.data = response_data
            return response
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


