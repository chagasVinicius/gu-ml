import pytest
from starlette.config import environ
from starlette.testclient import TestClient

environ["DB_HOST"] = "localhost"
environ["DB_USER"] = "gods"
environ["DB_PWD"] = "dbpwd"
environ["DB_NAME"] = "gods"

from gu_ml.main import get_app  # noqa: E402


@pytest.fixture()
def test_client():
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client
