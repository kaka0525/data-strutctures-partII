from __future__ import unicode_literals
from time import time
from random import shuffle


def merge_sort(init_list):
    if len(init_list) <= 1:
        return init_list
    list_left = init_list[:len(init_list) // 2]
    list_right = init_list[len(init_list) // 2:]
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
<<<<<<< HEAD
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
        merge_sort(test)
        worst_time = time() - t0
        print "A random list with {} entries, takes {} seconds with merge sort"\
            .format(iteration_list[count], worst_time)
=======
    def build_list(iterations):
        return_list = range(iterations)
        return return_list

    iteration_list = [10, 100, 1000, 10000]
    random_list = [[] for x in range(4)]
    sorted_list = [[] for x in range(4)]

    for i in range(len(iteration_list)):
        random_list[i].extend(build_list(iteration_list[i]))
        shuffle(random_list[i])
        sorted_list[i].extend(build_list(iteration_list[i]))

    count = 0
    for test in random_list:
        t0 = time()
        merge_sort(test)
        worst_time = time() - t0
        print "A random list with {} entries, takes {} seconds with mergesort"\
            .format(len(test), worst_time)
>>>>>>> 60f0f978c1f87de7a79e3b1469875c810292cae0
        count += 1

    count = 0
    for test in sorted_list:
        t0 = time()
        merge_sort(test)
        worst_time = time() - t0
        print "An already sorted list with {} entries, takes {} seconds with merge sort"\
<<<<<<< HEAD
            .format(iteration_list[count], worst_time)
=======
            .format(len(test), worst_time)
>>>>>>> 60f0f978c1f87de7a79e3b1469875c810292cae0
        count += 1
