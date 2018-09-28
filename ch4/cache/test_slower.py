import datetime
import pytest
import random
import time
from collections import namedtuple

Duration = namedtuple('Duration', ['current', 'last'])

@pytest.fixture(scope='session')
def duration_cache(request):
    key = 'duration/testdurations'
    d = Duration({}, request.config.cache.get(key, {}))
    yield d
    request.config.cache.set(key, d.current)

@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    d = duration_cache
    nodeid = request.node.nodeid
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()

    this_duration = (stop_time - start_time).total_seconds()
    d.current[nodeid] = this_duration
    last_duration = d.last.get(nodeid, None)
    if last_duration is not None:
        errorstring = "test duration over 2x last duration"
        assert this_duration <= last_duration * 2, errorstring

@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())
