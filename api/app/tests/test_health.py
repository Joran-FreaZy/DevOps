import pytest
from myapp.health import  status


def test_health():
    response, rc = status()
    assert "status" in response
    assert response["status"] == "ok"
    assert rc == 200
