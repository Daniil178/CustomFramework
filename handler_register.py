import importlib
from collections import defaultdict


def test():
    from views import hello
    print(hello())

def handler_register() -> dict[str, object]:
    module = importlib.import_module("views")
    g_dict = defaultdict(list)
    if not module:
        raise ModuleNotFoundError("No module named 'views.py'; 'views' is not a package")
    for o in dir(module):
        if not (o.startswith("__") and o.endswith("__")):
            o_func = getattr(module, o)
            print(o_func)
            g_dict[o_func.path].append(o_func)
    return g_dict

if __name__ == "__main__":
    test()