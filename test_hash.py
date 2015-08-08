from __future__ import unicode_literals
from hash import HashTable
import pytest


@pytest.fixture
def empty_hash():
    empty_hash = HashTable(16)
    return empty_hash


@pytest.fixture
def dict_hash():
    dict_hash = HashTable(1024)
    dictionary = open("/usr/share/dict/words", 'r')
    for word in dictionary:
        dict_hash.set(word.rstrip(), 1)
    return dict_hash


def test_hash(dict_hash):
    dictionary = open("/usr/share/dict/words", 'r')
    for word in dictionary:
        assert dict_hash.get(word.rstrip()) == 1


def test_empty(empty_hash):
    with pytest.raises(KeyError):
        empty_hash.get('a')
    empty_hash.hash('a')
    assert empty_hash.get('a') is None
    empty_hash.set('a', 15)
    assert empty_hash.get('a') == 15


def test_keysallowed(empty_hash):
    assert empty_hash.set('1', 12) is None
    assert empty_hash.set(b'1', 12) is None
    assert empty_hash.set(u'1', 12) is None
    with pytest.raises(TypeError):
        empty_hash.set(1, 12)


def test_valuesallowed(empty_hash):
    empty_hash.set('a', 12)
    assert empty_hash.get('a') == 12
    empty_hash.set('b', ['a', 7, 'abcd'])
    assert empty_hash.get('b') == ['a', 7, 'abcd']
    empty_hash.set('c', {'c': 37})
    assert empty_hash.get('c') == {'c': 37}
