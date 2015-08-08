from __future__ import unicode_literals
from radix_sort import radix_sort
from random import shuffle


def test_simple():
    simple_list = [10, 7, 8, 9, 2, 15, 0, 5]
    sorted_simple = radix_sort(simple_list)
    assert sorted_simple == sorted(simple_list)


def test_repeat():
    repeat_list = [10, 7, 8, 9, 2, 15, 0, 5, 15]
    sorted_repeat = radix_sort(repeat_list)
    assert sorted_repeat == sorted(repeat_list)


def test_already_sorted():
    already_sorted = [0, 2, 5, 7, 8, 9, 10, 15]
    sorted_already = radix_sort(already_sorted)
    assert sorted_already == sorted(already_sorted)


def test_reverse():
    reverse_list = [15, 10, 9, 8, 7, 5, 2, 0]
    sorted_reverse = radix_sort(reverse_list)
    assert sorted_reverse == sorted(reverse_list)


def test_long():
    long_list = range(10000)
    shuffle(long_list)
    sorted_long = radix_sort(long_list)
    assert sorted_long != long_list
    assert sorted_long == sorted(long_list)
