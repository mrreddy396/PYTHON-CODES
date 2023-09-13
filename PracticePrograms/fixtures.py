import pytest


@pytest.fixture
def setup_data():
    data = [1, 2, 3, 4, 5]
    return data


def test_list_length(setup_data):
    assert len(setup_data) == 5


def test_list_sum(setup_data):
    total = sum(setup_data)
    assert total == 15