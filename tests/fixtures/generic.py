from asyncio import get_event_loop

import pytest


@pytest.fixture(scope="module")
def event_loop():
    loop = get_event_loop()
    yield loop
    loop.close()
