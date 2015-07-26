from __future__ import unicode_literals
from bst import BST
import pytest

tree_val = [15, 7, 14, 16, 1, 5]


@pytest.fixture()
def empty_tree():
    tree = BST()
    return tree


@pytest.fixture()
def full_tree():
    tree = BST()
    for val in tree_val:
        tree.insert(val)
    return tree


def test_contains(full_tree):
    for val in tree_val:
        assert full_tree.contains(val)


def test_size(full_tree, empty_tree):
    assert full_tree.size() == (len(tree_val))
    assert empty_tree.size() == 0


def test_insert(full_tree, empty_tree):
    for val in tree_val:
        assert full_tree.contains(val)
    full_tree.insert(22)
    assert full_tree.contains(22)
    assert full_tree.size() == (len(tree_val) + 1)
    full_tree.insert(22)
    assert full_tree.size() == (len(tree_val) + 1)
    empty_tree.insert(5)
    assert empty_tree.size() == 1
    assert empty_tree.contains(5)


def test_depth(full_tree, empty_tree):
    assert full_tree.depth() == 4
    assert empty_tree.depth() == 0


def test_balance(full_tree, empty_tree):
    assert full_tree.balance() > 0
    assert empty_tree.balance() == 0
    empty_tree.insert(5)
    assert empty_tree.balance() == 0
    empty_tree.insert(8)
    assert empty_tree.balance() < 0
    empty_tree.insert(4)
    assert empty_tree.balance() == 0
    empty_tree.insert(1)
    assert empty_tree.balance() > 0


def test_pre_order(full_tree):
    g = full_tree.pre_order()
    assert list(g) == [15, 7, 1, 5, 14, 16]


def test_in_order(full_tree):
    g = full_tree.in_order()
    assert list(g) == [1, 5, 7, 14, 15, 16]


def test_post_order(full_tree):
    g = full_tree.post_order()
    assert list(g) == [5, 1, 14, 7, 16, 15]


def test_breadth_first(full_tree):
    g = full_tree.breadth_first()
    assert list(g) == [15, 7, 16, 1, 14, 5]
