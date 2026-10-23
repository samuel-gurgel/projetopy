import pytest
from fastapi.testclient import TestClient

from projetopy.app import app


@pytest.fixture
def client():
    return TestClient(app)
