from __future__ import unicode_literals
from insertion_sort import insertion_sort
<<<<<<< HEAD:test_insertion.py
=======
from random import shuffle
>>>>>>> 60f0f978c1f87de7a79e3b1469875c810292cae0:test_insertion.py


def test_simple():
    simple_list = [10, 7, 8, 9, 2, 15, 0, 5]
    sorted_simple = insertion_sort(simple_list)
<<<<<<< HEAD:test_insertion.py
=======
    assert sorted_simple != simple_list
>>>>>>> 60f0f978c1f87de7a79e3b1469875c810292cae0:test_insertion.py
    assert sorted_simple == sorted(simple_list)


def test_repeat():
    repeat_list = [10, 7, 8, 9, 2, 15, 0, 5, 15]
    sorted_repeat = insertion_sort(repeat_list)
<<<<<<< HEAD:test_insertion.py
=======
    assert sorted_repeat != repeat_list
>>>>>>> 60f0f978c1f87de7a79e3b1469875c810292cae0:test_insertion.py
    assert sorted_repeat == sorted(repeat_list)


def test_already_sorted():
    already_sorted = [0, 2, 5, 7, 8, 9, 10, 15]
    sorted_already = insertion_sort(already_sorted)
<<<<<<< HEAD:test_insertion.py
    assert sorted_already == sorted(already_sorted)
=======
    assert sorted_already == already_sorted
>>>>>>> 60f0f978c1f87de7a79e3b1469875c810292cae0:test_insertion.py


def test_reverse():
    reverse_list = [15, 10, 9, 8, 7, 5, 2, 0]
    sorted_reverse = insertion_sort(reverse_list)
<<<<<<< HEAD:test_insertion.py
=======
    assert sorted_reverse != reverse_list
>>>>>>> 60f0f978c1f87de7a79e3b1469875c810292cae0:test_insertion.py
    assert sorted_reverse == sorted(reverse_list)


def test_float():
    float_list = [10, 7, 8, 9.5, 2.5, 15, 0, 5]
    sorted_float = insertion_sort(float_list)
<<<<<<< HEAD:test_insertion.py
=======
    assert sorted_float != float_list
>>>>>>> 60f0f978c1f87de7a79e3b1469875c810292cae0:test_insertion.py
    assert sorted_float == sorted(float_list)


def test_long():
    long_list = range(10000)
    shuffle(long_list)
    sorted_long = insertion_sort(long_list)
    assert sorted_long != long_list
    assert sorted_long == sorted(long_list)
