from __future__ import unicode_literals
from time import time


def insertion_sort(init_list):
    return_list = init_list[:]
    for index in range(1, len(return_list)):
        value = return_list[index]
        i = index - 1
        while i >= 0:
            if value < return_list[i]:
                return_list[i + 1] = return_list[i]
                return_list[i] = value
                i = i - 1
            else:
                break
    return return_list


def merge_sort(init_list):
    if len(init_list) <= 1:
        return init_list
    list_left = init_list[:len(init_list)/2]
    list_right = init_list[len(init_list)/2:]
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
    insertion_sort(test_list)
    worst_time = time() - t0
    print "A reverse list perfomance with insertion sort: {} ".format(worst_time)

    test_list = best_case()
    t0 = time()
    insertion_sort(test_list)
    best_time = time() - t0
    print "A sorted list perfomance with insertion sort: {}".format(best_time)
