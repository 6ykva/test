from utils import dicts


def test_get_val():
    data = {
            'alex': 'friend',
            0: 'это число'}
    assert dicts.get_val(data, 'alex', 'git') == 'friend'
    assert dicts.get_val({}, 'alex', 'git') == 'git'
    assert dicts.get_val(data, 0, 'git') == 'это число'
    assert dicts.get_val(data, 'baralgin', 'git') == 'git'
    assert dicts.get_val(data, -1, 'git') == 'git'
