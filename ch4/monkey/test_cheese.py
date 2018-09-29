import cheese

def test_def_pref_full():
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual
