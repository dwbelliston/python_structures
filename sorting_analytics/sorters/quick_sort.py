import operator


# Heavy use of code found here:
# # http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
def quick_sort(list_data):
    quickSortHelper(list_data, 0, len(list_data)-1)
    return list_data


def quickSortHelper(list_data, first, last):
    if first < last:
        splitpoint = partition(list_data, first, last)
        quickSortHelper(list_data, first, splitpoint-1)
        quickSortHelper(list_data, splitpoint+1, last)


def partition(list_data, first, last):
    pivot_val = list_data[first]

    left_index = first+1
    right_index = last

    done = False
    while not done:

        # move left_index until you get something bigger than the pivot
        while left_index <= right_index and float(list_data[left_index]) <= float(pivot_val):
            left_index += 1

        # # move right_index until you get something smaller than the pivot
        while left_index <= right_index and float(list_data[right_index]) > float(pivot_val):
            right_index -= 1

        if left_index > right_index:
            done = True
        else:
            # exchange at the marks
            list_data[left_index], list_data[right_index] = list_data[right_index], list_data[left_index]

    list_data[first], list_data[right_index] = list_data[right_index], list_data[first]

    return right_index
