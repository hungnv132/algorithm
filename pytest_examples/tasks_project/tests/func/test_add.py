import pytest
from pytest_examples.tasks_project import tasks


def initialized_tasks_db(tmpdir):
    """Connect to db before testing and disconnet after."""

def test_add_return_valid_id():
    """ Metho task.add() should return an integer"""
    new_task = tasks.Task('do homework')
    task_id = tasks.add(new_task)

    assert isinstance(task_id, int)