import pytest
import tasks
from tasks import Task

def test_add_return_valid_id(tasks_db):
    """tasks.add(<valid task>) return an integer."""
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)
