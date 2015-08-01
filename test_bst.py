from __future__ import unicode_literals
from bst import BST
import pytest

tree_val = [15, 7, 14, 16, 1, 5]

<<<<<<< Updated upstream
=======
second_tree_val = [15, 7, 16, 5, 14, 3]

right_heavy_tree_val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

left_heavy_tree_val = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

double_left_rotation_tree_val = [10, 12, 11, 10.5]

double_right_rotation_tree_val = [10, 8, 9]

>>>>>>> Stashed changes

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


<<<<<<< Updated upstream
=======
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

>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======


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


def test_delete_root_node(full_tree):
    full_tree.delete(15)
    assert full_tree.size() == 5
    g = full_tree.in_order()
    assert list(g) == [1, 5, 7, 14, 16]
    assert full_tree.contains(15) is False


def test_balance_right_heavy_tree(right_heavy_tree):
    assert right_heavy_tree.size() == 10
>>>>>>> Stashed changes
