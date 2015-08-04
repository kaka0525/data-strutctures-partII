from __future__ import unicode_literals
from merge_sort import merge_sort


def test_merge_sort():
    simple_list = [10, 7, 8, 9, 2, 15, 0, 5]
    sorted_simple = merge_sort(simple_list)
    repeat_list = [10, 7, 8, 9, 2, 15, 0, 5, 15]
    sorted_repeat = merge_sort(repeat_list)
    already_sorted = [0, 2, 5, 7, 8, 9, 10, 15]
    sorted_already = merge_sort(already_sorted)
    reverse_list = [15, 10, 9, 8, 7, 5, 2, 0]
    sorted_reverse = merge_sort(reverse_list)
    float_list = [10, 7, 8, 9.5, 2.5, 15, 0, 5]
    sorted_float = merge_sort(float_list)
    assert sorted_simple == sorted(simple_list)
    assert sorted_repeat == sorted(repeat_list)
    assert sorted_already == sorted(already_sorted)
    assert sorted_reverse == sorted(reverse_list)
    assert sorted_float == sorted(float_list)
