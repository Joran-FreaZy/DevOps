import pytest
from myapp.math import random


@pytest.mark.parametrize("size", [1, 100])
def test_random(size):
    response, rc = random(size)
    assert "result" in response
    assert isinstance(response["result"], list)
    assert len(response["result"]) == size
    assert rc == 200


@pytest.mark.parametrize("size", [-42, 0])
def test_random_failure(size):
    response, rc = random(size)
    assert "caused_by" in response
    assert response["caused_by"] == "invalid size type"
    assert rc == 400
