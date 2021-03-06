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

if __name__ == '__main__':
    def worst_case(iterations):
        list_a = range(iterations)
        list_a.reverse()
        return list_a

    def best_case(iterations):
        list_b = range(iterations)
        return list_b

    iteration_list = [10, 100, 1000, 10000]
    random_list = [[] for x in range(4)]
    sorted_list = [[] for x in range(4)]

    for i in range(len(iteration_list)):
        random_list[i].extend(worst_case(iteration_list[i]))
        sorted_list[i].extend(best_case(iteration_list[i]))

    count = 0
    for test in random_list:
        t0 = time()
        insertion_sort(test)
        worst_time = time() - t0
        print "A reverse list with {} entries, takes {} seconds with insertion sort"\
            .format(iteration_list[count], worst_time)
        count += 1

    count = 0
    for test in sorted_list:
        t0 = time()
        insertion_sort(test)
        worst_time = time() - t0
        print "An already sorted list with {} entries, takes {} seconds with insertion sort"\
            .format(iteration_list[count], worst_time)
        count += 1
