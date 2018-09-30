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
