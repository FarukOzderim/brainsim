import pytest
from pydantic import ValidationError


async def test_example_fixture_usage(example_global_fixture):
    assert example_global_fixture == "example"


async def test_using_client_or_async_client_fixtures_in_unittest_automatically_skipped(async_client):
    print("This test must be skipped")

