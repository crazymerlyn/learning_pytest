import pytest

@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)
    return testdir

def test_pass_fail(sample_test):
    res = sample_test.runpytest()

    res.stdout.fnmatch_lines([
        u'*.F*',
    ])

    assert res.ret == 1

def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['*.O*',])
    assert result.ret == 1

def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('--nice', '-v')
    result.stdout.fnmatch_lines([
        '*::test_fail OPPORTUNITY for improvement*',
    ])
    assert result.ret == 1

def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines([
        '*::test_fail FAILED*',
    ])
    assert result.ret == 1

def test_header_nice(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['Thanks for running the tests.',])

def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    thanks_message = 'Thanks for running the tests.'
    assert thanks_message not in result.stdout.str()

def test_help_message(testdir):
    result = testdir.runpytest('--help')
    result.stdout.fnmatch_lines([
        'nice:',
        '*--nice*nice: turn FAILED into OPPORTUNITY for improvement',
    ])
