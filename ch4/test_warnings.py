import warnings
import pytest

def lame_function():
    warnings.warn('Please stop using this', DeprecationWarning)
    # rest of function

def test_lame_function(recwarn):
    lame_function()
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'
