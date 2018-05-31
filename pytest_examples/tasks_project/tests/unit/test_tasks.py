from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no parameters"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Check fields of namedtuple"""
    t = Task('go to school', 'hungnv132')
    assert t.summary == 'go to school'
    assert t.owner == 'hungnv132'
    assert (t.done, t.id) == (False, None)


def test_asdict():
    """ Method _asdict() should return a dictionnary"""
    t = Task('do homework', 'john', True, 88)
    d = t._asdict()
    expected_result = {
        'summary': 'do homework',
        'owner': 'john',
        'done': True,
        'id': 88
    }
    assert d == expected_result


def test_replace():
    """ Method replace() should change passed in fields"""
    t_before = Task('go shopping', 'terry', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('go shopping', 'terry', True, 10)
    assert t_after == t_expected



