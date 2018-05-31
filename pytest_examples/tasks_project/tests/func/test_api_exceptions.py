import pytest
from pytest_examples.tasks_project import tasks


@pytest.mark.smoke1
def test_list_raises():
    """ Method list() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """Method get() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


# Run : ​​pytest​-v​-m​'smoke'​test_api_exceptions.py​
# Run : ​​pytest​-v​-m​'get'​test_api_exceptions.py​
