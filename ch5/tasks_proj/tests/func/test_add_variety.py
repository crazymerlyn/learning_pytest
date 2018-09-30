import pytest
import tasks
from tasks import Task


def test_add_1():
    """tasks.get() using id returned from get() works."""
    task = Task('breathe', 'BRIAN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(task, t_from_db)

@pytest.mark.parametrize('task',
                         [Task('sleep', done=True),
                          Task('wake', 'brian'),
                          Task('breathe', 'BRIAN', True),
                          Task('exercise', 'BrIaN', False)])
def test_add_2(task):
    """Demonstrate parametrize with one parameter."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(task, t_from_db)

@pytest.mark.parametrize('summary, owner, done',
                         [('sleep', None, True),
                          ('wake', 'brian', False),
                          ('breathe', 'BRIAN', True),
                          ('exercise', 'BrIaN', False)])
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(task, t_from_db)

tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))
task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]

@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd:
    """Demonstrate parametrize and test classes."""

    def test_equivalent(self, task):
        """Similar test, just within a class."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """We can use the same data on multiple tests."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id


def equivalent(t1, t2):
    """Check two tasks for equivalence."""
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to the db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # This is where the testing happens

    tasks.stop_tasks_db()
