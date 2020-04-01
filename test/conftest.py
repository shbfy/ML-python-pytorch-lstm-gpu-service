import falcon
import pytest
from falcon import testing


@pytest.fixture(scope="session")
def client():
    """Client to call tests against"""
    return testing.TestClient(falcon.API())
