import importlib
from collections import defaultdict


def handler_register() -> dict[str, object]:
    module = importlib.import_module("views")
    g_dict = defaultdict(list)
    if not module:
        raise ModuleNotFoundError("No module named 'views.py'; 'views' is not a package")
    for o in dir(module):
        if not (o.startswith("__") and o.endswith("__")):
            g_dict[o].append(getattr(module, o))
    return g_dict
