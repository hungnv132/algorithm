import pytest


@pytest.fixture()
def the_data():
    """Return answer to ultimate question"""
    return 88


def test_some_data(the_data, fixture_session_scope):
    """User fixture return value in a test"""
    assert the_data == 88


def test_my_name(my_name):
    """use fixture in the file conftest.py"""
    assert my_name == 'hungnv132'