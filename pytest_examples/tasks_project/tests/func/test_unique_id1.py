import pytest
from pytest_examples.tasks_project import tasks


def test_unique_id():
    """Calling unquie_id twice should return diffrent numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

