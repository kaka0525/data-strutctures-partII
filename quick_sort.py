from __future__ import unicode_literals
from time import time
from random import shuffle


def quick_sort(init_list):
    _quick_sort2(init_list, 0, len(init_list) - 1)
    return init_list


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
    return(border)


if __name__ == '__main__':
    def worst_case(iterations):
        list_a = best_case(iterations)
        shuffle(list_a)
        return list_a

    def best_case(iterations):
        list_b = range(iterations)
        return list_b

    iteration_list = [10, 100, 1000, 10000]
    reverse_list = []
    sorted_list = []
    for iteration in iteration_list:
        reverse_list.append(worst_case(iteration))
        sorted_list.append(best_case(iteration))

    count = 0
    for test in reverse_list:
        t0 = time()
        quick_sort(test)
        worst_time = time() - t0
        print "A random list with {} entries, takes {} seconds with quick sort"\
            .format(iteration_list[count], worst_time)
        count += 1

    count = 0
    for test in sorted_list:
        t0 = time()
        quick_sort(test)
        worst_time = time() - t0
        print "An already sorted list with {} entries, takes {} seconds with quick sort"\
            .format(iteration_list[count], worst_time)
        count += 1
