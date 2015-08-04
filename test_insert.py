from __future__ import unicode_literals
from insertion_sort import insertion_sort


def test_insertion():
    simple_list = [10, 7, 8, 9, 2, 15, 0, 5]
    sort_simple_list = [10, 7, 8, 9, 2, 15, 0, 5]
    insertion_sort(simple_list)
    repeat_list = [10, 7, 8, 9, 2, 15, 0, 5, 15]
    sort_repeat_list = [10, 7, 8, 9, 2, 15, 0, 5, 15]
    insertion_sort(repeat_list)
    already_sorted = [0, 2, 5, 7, 8, 9, 10, 15]
    sort_already_sorted = [0, 2, 5, 7, 8, 9, 10, 15]
    insertion_sort(already_sorted)
    reverse_list = [15, 10, 9, 8, 7, 5, 2, 0]
    sort_reverse_list = [15, 10, 9, 8, 7, 5, 2, 0]
    insertion_sort(reverse_list)
    float_list = [10, 7, 8, 9.5, 2.5, 15, 0, 5]
    sort_float_list = [10, 7, 8, 9.5, 2.5, 15, 0, 5]
    insertion_sort(float_list)
    assert simple_list == sorted(sort_simple_list)
    assert repeat_list == sorted(sort_repeat_list)
    assert already_sorted == sorted(sort_already_sorted)
    assert reverse_list == sorted(sort_reverse_list)
    assert float_list == sorted(sort_float_list)
