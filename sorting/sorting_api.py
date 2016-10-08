import operator


# EX: bubble_sort(word_data, 'percent', 'desc')
def bubble_sort(list_sort, variable, direction):
    print('Bubbling! on:{} dir:{}'.format(variable, direction))

    op_funx = operator.ge if direction == 'asc' else operator.le

    # Need to pass through n-1 times, start high and go down
    # range(start, stop[, step])
    for i in range(len(list_sort) - 1, 0, -1):
        for j in range(i):
            current_val = getattr(list_sort[j], variable)
            next_val = getattr(list_sort[j + 1], variable)

            if op_funx(current_val,next_val):
                # Current, Next = Next, Current
                list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]

    return list_sort
