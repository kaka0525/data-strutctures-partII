from __future__ import unicode_literals
from bst import BST
import pytest

tree_val = [15, 7, 14, 16, 1, 5]

second_tree_val = [15, 7, 16, 5, 14, 3]

right_heavy_tree_val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

left_heavy_tree_val = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

double_left_rotation_tree_val = [15, 25, 16, 30, 24, 28]

double_right_rotation_tree_val = [14, 6, 10, 7, 3, 9, 8]


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


@pytest.fixture()
def second_full_tree():
    tree = BST()
    for val in second_tree_val:
        tree.insert(val)
    return tree


@pytest.fixture()
def right_heavy_tree():
    tree = BST()
    for val in right_heavy_tree_val:
        tree.insert(val)
    return tree


@pytest.fixture()
def left_heavy_tree():
    tree = BST()
    for val in left_heavy_tree_val:
        tree.insert(val)
    return tree


@pytest.fixture()
def double_left_rotation_tree():
    tree = BST()
    for val in double_left_rotation_tree_val:
        tree.insert(val)
    return tree


@pytest.fixture()
def double_right_rotation_tree():
    tree = BST()
    for val in double_right_rotation_tree_val:
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
    assert full_tree.depth() == 3
    assert empty_tree.depth() == 0


def test_balance(full_tree, empty_tree):
    assert full_tree.balance() == 0
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
    assert list(g) == [14, 5, 1, 7, 15, 16]


def test_in_order(full_tree):
    g = full_tree.in_order()
    assert list(g) == [1, 5, 7, 14, 15, 16]


def test_post_order(full_tree):
    g = full_tree.post_order()
    assert list(g) == [1, 7, 5, 16, 15, 14]


def test_breadth_first(full_tree):
    g = full_tree.breadth_first()
    assert list(g) == [14, 5, 15, 1, 7, 16]


def test_delete_leaf(full_tree):
    full_tree.delete(16)
    assert full_tree.size() == 5
    g = full_tree.in_order()
    assert list(g) == [1, 5, 7, 14, 15]
    assert full_tree.contains(16) is False


def test_delete_node_with_one_right_child(full_tree):
    full_tree.delete(1)
    assert full_tree.size() == 5
    g = full_tree.in_order()
    assert list(g) == [5, 7, 14, 15, 16]
    assert full_tree.contains(1) is False


def test_delete_node_with_one_left_child(second_full_tree):
    second_full_tree.delete(5)
    assert second_full_tree.size() == 5
    g = second_full_tree.in_order()
    assert list(g) == [3, 7, 14, 15, 16]
    assert second_full_tree.contains(5) is False


def test_delete_node_with_two_child(full_tree):
    full_tree.delete(7)
    assert full_tree.size() == 5
    g = full_tree.in_order()
    assert list(g) == [1, 5, 14, 15, 16]
    assert full_tree.contains(7) is False


def test_delete_middle_of_tree():
    t = BST()
    t.insert(3)
    t.insert(2)
    t.insert(5)
    t.insert(1)
    t.insert(4)
    t.insert(6)
    t.insert(7)
    t.delete(5)
    assert list(t.pre_order()) == [3, 2, 1, 6, 4, 7]


def test_delete_root_node(full_tree):
    full_tree.delete(15)
    assert full_tree.size() == 5
    g = full_tree.in_order()
    assert list(g) == [1, 5, 7, 14, 16]
    assert full_tree.contains(15) is False


def test_balance_right_heavy_tree(right_heavy_tree):
    g = right_heavy_tree.pre_order()
    p = right_heavy_tree.post_order()
    assert list(g) == [4, 2, 1, 3, 8, 6, 5, 7, 9, 10]
    assert list(p) == [1, 3, 2, 5, 7, 6, 10, 9, 8, 4]
    assert right_heavy_tree.balance() < 2


def test_balance_left_heavy_tree(left_heavy_tree):
    g = left_heavy_tree.pre_order()
    p = left_heavy_tree.post_order()
    assert list(g) == [7, 3, 2, 1, 5, 4, 6, 9, 8, 10]
    assert list(p) == [1, 2, 4, 6, 5, 3, 8, 10, 9, 7]
    assert left_heavy_tree.balance() < 2


def test_double_right_rotation_tree(double_right_rotation_tree):
    g = double_right_rotation_tree.pre_order()
    p = double_right_rotation_tree.post_order()
    assert list(g) == [7, 6, 3, 10, 9, 8, 14]
    assert list(p) == [3, 6, 8, 9, 14, 10, 7]
    assert double_right_rotation_tree.balance() < 2


def test_double_left_rotation_tree(double_left_rotation_tree):
    g = double_left_rotation_tree.pre_order()
    p = double_left_rotation_tree.post_order()
    assert list(g) == [25, 16, 15, 24, 30, 28]
    assert list(p) == [15, 24, 16, 28, 30, 25]
    assert double_left_rotation_tree.balance() < 2
