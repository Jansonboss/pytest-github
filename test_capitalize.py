
def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.capitalize()

def lower_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.lower()

def test_capitalize_string():
    assert capitalize_string('test') == 'Test'

def test_lowercase_string():
	assert lower_string('test') == 'test'

def test__string():
	assert 'test' == 'test'