import operator


''' sort_by_order = [
        {'name': 'percent', 'dir': 'asc'},
        {'name': 'count', 'dir': 'asc'},
        {'name': 'word', 'dir': 'desc'}
    ]
    bubble_sort(word_data, sort_by_order)
'''
def bubble_sort(list_sort, sortby_order):
    # print('Bubbling! on:{} '.format(sortby_order))

    # Need to pass through n-1 times, start high and go down
    # range(start, stop[, step])
    for i in range(len(list_sort) - 1, 0, -1):
        for j in range(i):
            # bool_keep_sorting if operator results in equal
            bool_keep_sorting = True
            sortby_index = 0

            while bool_keep_sorting:
                current_val = getattr(list_sort[j], sortby_order[sortby_index]['name'])
                next_val = getattr(list_sort[j + 1], sortby_order[sortby_index]['name'])

                # Get operator to decide desc vs asc
                op_funx = operator.gt if sortby_order[sortby_index]['dir'] == 'asc' else operator.lt

                # Check main operator (>, or <)
                if op_funx(current_val, next_val):
                    # Current, Next = Next, Current
                    list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]

                # Check if next sort is needed
                elif operator.eq(current_val, next_val):
                    # Values are equal, proceed to next sort
                    if sortby_index < len(sortby_order) - 1:
                        sortby_index += 1
                    else:
                        # Exhausted all sortby vars, deep equals
                        bool_keep_sorting = False
                # Values stay in place
                else:
                    bool_keep_sorting = False

    return list_sort
