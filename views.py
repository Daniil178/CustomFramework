from handler import Request
import json

@Request(method="get", url_path="/hello")
def hello():
    return json.loads({"msg", "hello world"})