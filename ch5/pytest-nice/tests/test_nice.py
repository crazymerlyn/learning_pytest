def test_pass_fail(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)

    res = testdir.runpytest()

    res.stdout.fnmatch_lines([
        u'*.F*',
    ])

    assert res.ret == 1
