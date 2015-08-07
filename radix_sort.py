from math import floor, log10


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
        if order_mag < int(floor(log10(number))):
            order_mag = int(floor(log10(number)))
    return order_mag
