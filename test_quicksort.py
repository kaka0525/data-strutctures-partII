from __future__ import unicode_literals
from quick_sort import quick_sort
from random import shuffle


def test_simple():
    simple_list = [10, 7, 8, 9, 2, 15, 0, 5]
    sorted_simple = quick_sort(simple_list)
    assert sorted_simple == sorted(simple_list)


def test_repeat():
    repeat_list = [10, 7, 8, 9, 2, 15, 0, 5, 15]
    sorted_repeat = quick_sort(repeat_list)
    assert sorted_repeat == sorted(repeat_list)


def test_already_sorted():
    already_sorted = [0, 2, 5, 7, 8, 9, 10, 15]
    sorted_already = quick_sort(already_sorted)
    assert sorted_already == sorted(already_sorted)


def test_reverse():
    reverse_list = [15, 10, 9, 8, 7, 5, 2, 0]
    sorted_reverse = quick_sort(reverse_list)
    assert sorted_reverse == sorted(reverse_list)


def test_float():
    float_list = [10, 7, 8, 9.5, 2.5, 15, 0, 5]
    sorted_float = quick_sort(float_list)
    assert sorted_float == sorted(float_list)


def test_long():
    long_list = range(10000)
    shuffle(long_list)
    sorted_long = quick_sort(long_list)
    assert sorted_long != long_list
    assert sorted_long == sorted(long_list)

