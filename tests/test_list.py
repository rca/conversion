import datetime

from nose.tools import assert_equal

from conversion import convert_list


def test_delimiter():
    """
    Ensure the delimiter kwarg is used
    """
    assert_equal(["a", "b"], convert_list("a:b", delimiter=":"))


def test_single_element():
    """
    Ensure a string without a delimiter is returned as a single element list
    """
    assert_equal(["a"], convert_list("a"))


def test_split_and_stripped():
    """
    Ensure spaces are stripped off values
    """
    assert_equal(["a", "b"], convert_list("a, b"))
