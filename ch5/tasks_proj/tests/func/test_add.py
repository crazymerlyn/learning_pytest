import pytest
import tasks
from tasks import Task

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to the db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # This is where the testing happens

    tasks.stop_tasks_db()

def test_add_returns_valid_id():
    """tasks.add(<valid task>) should return an integer."""
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)

@pytest.mark.smoke
def test_added_task_has_id_set():
    """task_id field is set by tasks.add()."""
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    task_from_db = tasks.get(task_id)

    assert task_from_db.id == task_id
