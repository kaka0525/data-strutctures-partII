from __future__ import unicode_literals
from time import time


def merge_sort(init_list):
    if len(init_list) <= 1:
        return init_list
    list_left = init_list[:len(init_list) / 2]
    list_right = init_list[len(init_list) / 2:]
    left = merge_sort(list_left)
    right = merge_sort(list_right)
    return merge(left, right)


def merge(left, right):
    return_list = []
    while left and right:
        if left[0] <= right[0]:
            return_list.append(left[0])
            left = left[1:]
        else:
            return_list.append(right[0])
            right = right[1:]
    while left:
        return_list.append(left[0])
        left = left[1:]
    while right:
        return_list.append(right[0])
        right = right[1:]
    return return_list


if __name__ == '__main__':
    def worst_case():
        list_a = range(100)
        list_a.reverse()
        return list_a

    def best_case():
        list_b = range(100)
        return list_b

    test_list = worst_case()
    t0 = time()
    merge_sort(test_list)
    worst_time = time() - t0
    print "A reverse list perfomance with merge sort: {} ".format(worst_time)

    test_list = best_case()
    t0 = time()
    merge_sort(test_list)
    best_time = time() - t0
    print "A sorted list perfomance with merge sort: {}".format(best_time)
