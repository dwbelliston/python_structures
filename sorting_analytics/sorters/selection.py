import operator


def selection_sort(list_data):
    # Start at right, place at (n - i) eg: 9, 8, 7 etc..
    # # end at -1 so it hits 0
    for i in range(len(list_data) - 1, -1, -1):

        # start with the place index (far right) as largest
        largest_val_index = i

        for j in range(0, i):
                # grab the values for current and largest based on sort level
                current_val = list_data[j]
                largest_val = list_data[largest_val_index]

                # Check main operator (>, or <)
                if int(current_val) >= int(largest_val):
                    # track the new largest index, and move to next
                    largest_val_index = j

        # place_val, largest_val = largest_val, place_val
        list_data[i], list_data[largest_val_index] = list_data[largest_val_index], list_data[i]

    return list_data
