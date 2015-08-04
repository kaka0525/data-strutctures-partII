from __future__ import unicode_literals
from time import time


def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i + 1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break


if __name__ == '__main__':
    def worst_case():
        list_a = range(100)
        list_a = list_a.reverse()
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
