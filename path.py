from  request_class import Request
from responce_class import Response
from status import HTTP_STATUS
import re

def path(payload: str, Giga_dict):
    clown_list = payload("\n")
    first_str = clown_list[0].split()
    method = first_str[0]

    request = Request()
    request.header = clown_list[1:-1],
    request.method = method,
    request.content_type = clown_list[-1],
    request.url = first_str[1]

    url_path = request.url
    get_args = (url_path[url_path.index("?"): -1])[1:-1] if url_path.index("?") != -1 else None
    param_temp = url_path[0:url_path.index("?") - 1]
    param = param_temp[param_temp.rindex("/") + 1:-1] if get_args else url_path[url_path.rindex("/"):-1]
    path = url_path
    for key, values in Giga_dict.items():
        if key in request.url:
            for value in values:
                if value.param == param:
                    response = value(request, response)
                    break
    else:
        response = Response()
        Response.status = HTTP_STATUS.HTTP_404_NOT_FOUND
    return response




