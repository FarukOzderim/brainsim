import pytest


@pytest.fixture
def example_global_fixture():
    value = "example"
    yield value
