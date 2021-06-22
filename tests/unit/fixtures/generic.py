import pytest


@pytest.fixture
async def client():
    pytest.skip("Client is NOT available for unittests")
