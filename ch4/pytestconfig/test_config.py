import pytest

@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo

@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt

def test_option(foo, myopt):
    print('"foo" set to:', foo)
    print('"myopt" set to:', myopt)
