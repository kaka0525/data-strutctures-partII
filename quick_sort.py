from __future__ import unicode_literals
from time import time
from random import shuffle


def quick_sort(init_list):
    return_list = init_list[:]
    _quick_sort2(return_list, 0, len(return_list) - 1)
    return return_list


def _quick_sort2(init_list, low, high):
    if low < high:  # if there's more than one item to be sorted
        p = _partition(init_list, low, high)
        _quick_sort2(init_list, low, p - 1)
        _quick_sort2(init_list, p + 1, high)


def _get_pivot(init_list, low, high):
    mid_idx = (high + low) // 2
    pivot = high
    if init_list[low] < init_list[mid_idx]:
        if init_list[mid_idx] < init_list[high]:
            pivot = mid_idx
    elif init_list[low] < init_list[high]:
        pivot = low
    return pivot


def _partition(init_list, low, high):
    pivot_idx = _get_pivot(init_list, low, high)
    pivot_value = init_list[pivot_idx]
    init_list[pivot_idx], init_list[low] = init_list[low], init_list[pivot_idx]
    border = low

    for i in range(low, high + 1):
        if init_list[i] < pivot_value:
            border += 1
            init_list[i], init_list[border] = init_list[border], init_list[i]
    init_list[low], init_list[border] = init_list[border], init_list[low]
    return border


if __name__ == '__main__':
    def build_list(iterations):
        return_list = range(iterations)
        return return_list

    iteration_list = [10, 100, 1000, 10000]
    random_list = [[] for x in range(4)]
    sorted_list = [[] for x in range(4)]

    for i in range(len(iteration_list)):
        random_list[i].extend(build_list(iteration_list[i]))
        shuffle(random_list)
        sorted_list[i].extend(build_list(iteration_list[i]))

    count = 0
    for test in random_list:
        t0 = time()
        quick_sort(test)
        worst_time = time() - t0
        print "A random list with {} entries, takes {} seconds with quick sort"\
            .format(len(test), worst_time)
        count += 1

    count = 0
    for test in sorted_list:
        t0 = time()
        quick_sort(test)
        worst_time = time() - t0
        print "An already sorted list with {} entries, takes {} seconds with quick sort"\
            .format(len(test), worst_time)
        count += 1
