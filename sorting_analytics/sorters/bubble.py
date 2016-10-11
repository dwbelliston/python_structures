import operator


def bubble_sort(list_data):
    # Need to pass through n-1 times, start high and go down
    # range(start, stop[, step])
    for i in range(len(list_data) - 1, 0, -1):
        for j in range(i):

            current_val = list_data[j]
            next_val = list_data[j + 1]

            # Check main operator (>, or <)
            if int(current_val) >= int(next_val):
                # Current, Next = Next, Current
                list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]

    return list_data
