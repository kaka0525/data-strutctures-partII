def quick_sort(init_list):
    _quick_sort2(init_list, 0, len(init_list) - 1)


def _quick_sort2(init_list, low_index, high_index):
    if low_index < high_index:  # if there's more than one item to be sorted
        p = _partition(init_list, low_index, high_index)
        _quick_sort2(init_list, low_index, p - 1)
        _quick_sort2(init_list, p + 1, high_index)


def _get_pivot(init_list, low_index, high_index):
    mid_index = (high_index + low_index) // 2
    pivot = high_index
    if init_list[low_index] < init_list[mid_index]:
        if init_list[mid_index] < init_list[high_index]:
            pivot = mid_index
    elif init_list[low_index] < init_list[high_index]:
        pivot = low_index
    return pivot


def _partition(init_list, low_index, high_index):
    pivot_index = _get_pivot(init_list, low_index, high_index)
    pivot_value = init_list[pivot_index]
    init_list[pivot_index], init_list[low_index] = init_list[low_index],
    init_list[pivot_index]
    border = low_index

    for i in range(low_index, high_index + 1):
        if init_list[i] < pivot_value:
            border += 1
            init_list[i], init_list[border] = init_list[border], init_list[i]
    init_list[low_index], init_list[border] = init_list[border],
    init_list[low_index]
