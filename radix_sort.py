from __future__ import unicode_literals
from math import floor, log10
from time import time


def radix_sort(initial_list):
    order_mag = _order_mag(initial_list)
    return_list = initial_list[:]
    for i in range(order_mag+1):
        buckets = [[] for x in range(10)]
        for number in return_list:
            buckets[(number // (10**i)) % 10].append(number)
        return_list = []
        for bucket in buckets:
            return_list.extend(bucket)
    return return_list


def _order_mag(initial_list):
    order_mag = 0
    for number in initial_list:
        try:
            if order_mag < int(floor(log10(number))):
                order_mag = int(floor(log10(number)))
        except:
            pass
    return order_mag


if __name__ == '__main__':
    def build_list(list_len, max_val):
        return_list = []
        for i in range(list_len):
            return_list.append(i % 10)
        return_list.append(max_val)
        return return_list

    iteration_list = [10, 100, 1000, 10000]
    best_list = [[] for x in range(4)]
    worst_list = [[] for x in range(4)]

    for i in range(len(iteration_list)):
        best_list[i].extend(build_list(iteration_list[i], 9))
        worst_list[i].extend(build_list(iteration_list[i], 98765))

    for i in range(len(best_list)):
        t0 = time()
        radix_sort(best_list[i])
        worst_time = time() - t0
        print "A list of {} entries and max value of 9, using radix sort , takes {} seconds with radix sort"\
            .format(len(best_list[i]), worst_time)

    for i in range(len(worst_list)):
        t0 = time()
        radix_sort(worst_list[i])
        worst_time = time() - t0
        print "A list of {} entries and max value of 98765, using radix sort , takes {} seconds with radix sort"\
            .format(len(worst_list[i]), worst_time)
