import inspect

from .fixtures import *


def pytest_collection_modifyitems(items):
    for item in items:
        if inspect.iscoroutinefunction(item.function):
            item.add_marker('asyncio')
