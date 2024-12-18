from pprint import pprint
import inspect
import random
import math


def introspection_info(obj: object) -> dict:
    module = inspect.getmodule(obj)
    attrs = {
        "type": type(obj).__name__,
        "attributes": [],
        "methods": [],
        "module": module.__name__ if module else None,
    }
    for name, value in inspect.getmembers(obj):
        if callable(value):
            attrs["methods"].append(name)
        else:
            attrs["attributes"].append(name)
    return attrs


if __name__ == "__main__":
    pprint(introspection_info(random.choice))
    pprint(introspection_info(math.pi))
    pprint(introspection_info(42))
