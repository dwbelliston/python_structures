#!/usr/bin/env python3

def merge_lists(list1=[], list2=[], keys=['percent', 'count', 'word']):
    '''Merges two sorted lists into a new, sorted list.  The new list is sorted by percent, count, alpha.'''

    """
    >>> a = [1, 3, 5, 7]
    >>> b = [2, 4, 6, 8]
    >>> [i for i in linear_merge(a, b)]
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> [i for i in linear_merge(b, a)]
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> a = [1, 2, 2, 3]
    >>> b = [2, 2, 4, 4]
    >>> [i for i in linear_merge(a, b)]
    [1, 2, 2, 2, 2, 3, 4, 4]
    """
    for i in list1:
        print(i)
    # list1 = iter(list1)
    # list2 = iter(list2)
    #
    # value1 = next(list1)
    # value2 = next(list2)
    #
    # # We'll normally exit this loop from a next() call raising StopIteration, which is
    # # how a generator function exits anyway.
    # while True:
    #     if value1 <= value2:
    #         # Yield the lower value.
    #         yield value1
    #         try:
    #             # Grab the next value from list1.
    #             value1 = next(list1)
    #         except StopIteration:
    #             # list1 is empty.  Yield the last value we received from list2, then
    #             # yield the rest of list2.
    #             yield value2
    #             while True:
    #                 yield next(list2)
    #     else:
    #         yield value2
    #         try:
    #             value2 = next(list2)
    #
    #         except StopIteration:
    #             # list2 is empty.
    #             yield value1
    #             while True:
    #                 yield next(list1)
    #



















    # new_master = []
    #
    # if not len(list1) or not len(list2):
    #     return list1 + list2
    #
    # # both lists have len() at this point
    # val_1 = list1.pop(0)
    # val_2 = list2.pop(0)
    #
    # keep_merging = True
    #
    # key_index = 0
    #
    # while keep_merging:
    #
    #     # add val_1 if its bigger
    #     if getattr(val_1, keys[key_index]) > getattr(val_2, keys[key_index]):
    #         key_index = 0
    #         # put val_1 in the list
    #         new_master.append(val_1)
    #         # check if there is more in list1
    #         try:
    #             val_1 = list1.pop(0)
    #         except IndexError:
    #             new_master.extend(list2)
    #             keep_merging = False
    #
    #     # add val_2 if its bigger
    #     elif getattr(val_1, keys[key_index]) < getattr(val_2, keys[key_index]):
    #         key_index = 0
    #         # put val_2 in the list
    #         new_master.append(val_2)
    #         # check if there is more in list1
    #         try:
    #             val_2 = list2.pop(0)
    #         except IndexError:
    #             new_master.extend(list1)
    #             keep_merging = False
    #
    #     # equal, try next level of compare
    #     else:
    #         if key_index < len(keys) - 1:
    #             key_index += 1
    #         else:
    #             # deep equals, just add val_1
    #             key_index = 0
    #
    #             # put val_1 in the list
    #             new_master.append(val_1)
    #             # check if there is more in list1
    #             try:
    #                 val_1 = list1.pop(0)
    #             except IndexError:
    #                 new_master.extend(list2)
    #                 keep_merging = False
    #
    # return new_master
