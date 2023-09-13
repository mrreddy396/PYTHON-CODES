import pytest


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (5, 7, 12), (10, 20, 30)])
def test_addition_parametrized(a, b, expected):
    result = a + b
    assert result == expected
