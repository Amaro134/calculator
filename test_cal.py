# import pytest
from cal import get_numbers, add_numbers, multiply_numbers
from unittest.mock import patch


@patch('builtins.input', side_effect=['5', '10', 'done'])
def test_get_numbers_valid(mock_input):
    result = get_numbers()
    assert result == [5.0, 10.0]


@patch('builtins.input', side_effect=['5', 'abc', '10', 'done'])
def test_get_numbers_with_invalid(mock_input):
    result = get_numbers()
    assert result == [5.0, 10.0]


def test_add_numbers_single():
    assert add_numbers([5]) == 5


def test_add_numbers_empty():
    assert add_numbers([]) == 0


def test_add_numbers_positive():
    assert multiply_numbers([2, 3, 4]) == 24
    assert multiply_numbers([2, 10]) == 20


def test_multiply_numbers_positive():
    assert multiply_numbers([2, 3, 4]) == 24
    assert multiply_numbers([2, 10]) == 20


def test_multiply_numbers_by_zero():
    assert multiply_numbers([2, 0]) == 0
    assert multiply_numbers([1, 2, 0]) == 0


def test_multiply_numbers_single():
    # test multiply numbers with single number
    assert multiply_numbers([1]) == 1
    assert multiply_numbers([5]) == 5


def test_multiply_numbers_negative():
    # test multiply numbers negative
    assert multiply_numbers([2, -10]) == -20
    assert multiply_numbers([-4, -4]) == 16
