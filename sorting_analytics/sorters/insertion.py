import operator


def insertion_sort(list_data):
    # print('Insertion! on:{} '.format(sortby_order))
    for i in range(1, len(list_data)):
        # Check to exchange to the left until it inserts
        while i > 0:

            # Get the pair
            insert_val = list_data[i]
            prev_val = list_data[i - 1]

            # If smaller than left, exchange places
            if int(insert_val) <= int(prev_val):
                # prev_val, insert_val = insert_val, prev_val
                list_data[i - 1], list_data[i] = list_data[i], list_data[i - 1]

            i -= 1

    return list_data
