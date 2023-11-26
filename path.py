#/fgdo/dfgdf/cwe
def path(payload: str, Giga_dict):
    clown_list = payload("\n")
    first_str = clown_list[0].split()
    method = first_str[0]

    data_dict = {
        "header":
            clown_list[1:-1],
        "method":
            method,
        "content_type":
            clown_list[-1],
        'url' :
            first_str[1]
    }
    url_path = data_dict["url"]
    get_args = (url_path[url_path.index("?"): -1])[1:-1] if url_path.index("?") != -1 else None
    param_temp = url_path[0:url_path.index("?") - 1]
    param = param_temp[param_temp.rindex("/") + 1:-1] if get_args else url_path[url_path.rindex("/"):-1]
    path = url_path
    for key, value in Giga_dict.items():
        if key in data_dict.get('url'):
            for value in values:
                if value.param == param:
                    value()
                    break
    data_dict["status"] = 500
    return data_dict




