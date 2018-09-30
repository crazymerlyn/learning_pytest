import pytest
import tasks
from tasks import Task

@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id_1():
    """Calling unique id twice should return different numbers."""
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2

def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))

    uid = tasks.unique_id()
    assert uid not in ids

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to the db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # This is where the testing happens

    tasks.stop_tasks_db()
