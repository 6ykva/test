import pytest
from utils import arrs


@pytest.fixture
def test_fixture():
    return [1, 2, 3, 4]


def test_get(test_fixture):
    assert arrs.get(test_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(test_fixture):
    assert arrs.my_slice(test_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(test_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(test_fixture) == [1, 2, 3, 4]
    assert arrs.my_slice([]) == []
