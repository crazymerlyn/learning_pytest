import pytest
import tasks
from tasks import Task

@pytest.mark.usefixtures('tasks_db')
class TestAdd:
    """Tests related to tasks.add()."""

    def test_missing_summary(self):
        """Raises an exception if summary is missing."""
        with pytest.raises(ValueError):
            tasks.add(Task(owner='bob'))

    def test_done_not_bool(self):
        """Raises an exception if done is not a bool."""
        with pytest.raises(ValueError):
            tasks.add(Task(summary='summary', done='True'))

def test_add_raises():
    """add() raises an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')

def test_start_tasks_db_raises():
    """Unsupported db raises an exception."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"

@pytest.mark.smoke
def test_list_raises():
    """list() raises an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)

@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() raises an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


class TestUpdate:
    """Test expected exceptions with tasks.update()."""

    def test_bad_id(self):
        """A non-int id raises an exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict_instead': 1}, task=tasks.Task())

    def test_bad_task(self):
        """A non-Task task raises an exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')
