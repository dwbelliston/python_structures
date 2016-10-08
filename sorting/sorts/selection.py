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

        largest_val_index = i
        largest_val = getattr(list_sort[largest_val_index], sortby_order[0]['name'])

        # find largest in range (n - i), items on right will be placed-dont check
        for j in range(0, i):
            current_val = getattr(list_sort[j], sortby_order[0]['name'])
            if current_val > largest_val:
                largest_val_index = j
                largest_val = current_val

        # place_val, largest_val = largest_val, place_val
        list_sort[i], list_sort[largest_val_index] = list_sort[largest_val_index], list_sort[i]


    return list_sort
