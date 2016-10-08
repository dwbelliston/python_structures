import operator


''' sort_by_order = [
        {'name': 'percent', 'dir': 'asc'},
        {'name': 'count', 'dir': 'asc'},
        {'name': 'word', 'dir': 'desc'}
    ]
    selection_sort(word_data, sort_by_order)
'''
def selection_sort(list_sort, sortby_order):
    print('Selection! on:{} '.format(sortby_order))

    # Start at right, place at (n - i) eg: 9, 8, 7 etc..
    # # end at -1 so it hits 0
    for i in range(len(list_sort) - 1, -1, -1):

        # start with the place index (far right) as largest
        largest_val_index = i

        for j in range(0, i):
            # bool_keep_sorting if operator results in equal to do a deep sort
            bool_keep_sorting = True
            sortby_index = 0

            while bool_keep_sorting:
                # grab the values for current and largest based on sort level
                current_val = getattr(list_sort[j], sortby_order[sortby_index]['name'])
                largest_val = getattr(list_sort[largest_val_index], sortby_order[sortby_index]['name'])
                # print('COMPARING CUR:{}:{} --- LARG:{}:{}'.format(j, current_val, largest_val_index, largest_val))

                # Get operator to decide desc vs asc
                op_funx = operator.gt if sortby_order[sortby_index]['dir'] == 'asc' else operator.lt

                # Check main operator (>, or <)
                if op_funx(current_val, largest_val):
                    # track the new largest index, and move to next
                    largest_val_index = j
                    bool_keep_sorting = False

                # Check if next sort is needed
                elif operator.eq(current_val, largest_val):
                    # Values are equal, proceed to next sort
                    if sortby_index < len(sortby_order) - 1:
                        sortby_index += 1
                    else:
                        # Exhausted all sortby vars, deep equals
                        bool_keep_sorting = False
                # Values stay in place
                else:
                    bool_keep_sorting = False

        # place_val, largest_val = largest_val, place_val
        list_sort[i], list_sort[largest_val_index] = list_sort[largest_val_index], list_sort[i]

    return list_sort
