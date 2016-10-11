#!/usr/bin/env python3

def merge_lists(list1=[], list2=[], keys=['percent', 'count', 'word']):
    '''Merges two sorted lists into a new, sorted list.  The new list is sorted by percent, count, alpha.'''
    new_master = []

    if not len(list1) or not len(list2):
        return list1 + list2

    # both lists have len() at this point
    val_1 = list1.pop(0)
    val_2 = list2.pop(0)

    keep_merging = True

    key_index = 0

    while keep_merging:

        # add val_1 if its bigger
        if getattr(val_1, keys[key_index]) > getattr(val_2, keys[key_index]):
            key_index = 0
            # put val_1 in the list
            new_master.append(val_1)
            # check if there is more in list1
            try:
                val_1 = list1.pop(0)
            except IndexError:
                new_master.extend(list2)
                keep_merging = False

        # add val_2 if its bigger
        elif getattr(val_1, keys[key_index]) < getattr(val_2, keys[key_index]):
            key_index = 0
            # put val_2 in the list
            new_master.append(val_2)
            # check if there is more in list1
            try:
                val_2 = list2.pop(0)
            except IndexError:
                new_master.extend(list1)
                keep_merging = False

        # equal, try next level of compare
        else:
            if key_index < len(keys) - 1:
                key_index += 1
            else:
                # deep equals, just add val_1
                key_index = 0

                # put val_1 in the list
                new_master.append(val_1)
                # check if there is more in list1
                try:
                    val_1 = list1.pop(0)
                except IndexError:
                    new_master.extend(list2)
                    keep_merging = False

    return new_master
