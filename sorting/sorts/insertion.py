import operator


''' sort_by_order = [
        {'name': 'percent', 'dir': 'asc'},
        {'name': 'count', 'dir': 'asc'},
        {'name': 'word', 'dir': 'desc'}
    ]
    insertion_sort(word_data, sort_by_order)
'''
def insertion_sort(list_sort, sortby_order):
    print('Insertion! on:{} '.format(sortby_order))
    for i in range(1, len(list_sort)):

        bool_looking = True
        # Check to exchange to the left until it inserts
        while i > 0 and bool_looking:

            bool_keep_sorting = True
            sortby_index = 0
            while bool_keep_sorting:
                # Get the pair
                insert_val = getattr(list_sort[i], sortby_order[sortby_index]['name'])
                prev_val = getattr(list_sort[i - 1], sortby_order[sortby_index]['name'])

                # Get operator to decide desc vs asc
                op_funx = operator.gt if sortby_order[sortby_index]['dir'] == 'desc' else operator.lt

                # If smaller than left, exchange places
                if op_funx(insert_val, prev_val):
                    list_sort[i - 1], list_sort[i] = list_sort[i], list_sort[i - 1]
                # Check if next sort is needed
                elif operator.eq(insert_val, prev_val):
                    # Values are equal, proceed to next sort
                    if sortby_index < len(sortby_order) - 1:
                        sortby_index += 1
                    else:
                        # Exhausted all sortby vars, deep equals
                        bool_keep_sorting = False
                # Values stay in place
                else:
                    bool_keep_sorting = False

            i -= 1

    return list_sort
