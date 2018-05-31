import pytest


@pytest.fixture()
def my_name():
    return 'hungnv132'


@pytest.fixture(scope='session')
def fixture_session_scope():
    print("Fixture scope session")
