#!/usr/bin/env python3

def merge_lists(list1, list2):
    '''Merges two sorted lists into a new, sorted list.  The new list is sorted by percent, count, alpha.'''
    list1 = iter(list1)
    list2 = iter(list2)

    # check list 1, return all of 2 if no list 1
    try:
        value1 = next(list1)
    except StopIteration:
        while True:
            yield next(list2)

    # check list 2, return all of 1 if no list 2
    try:
        value2 = next(list2)
    except StopIteration:
        yield value1
        while True:
            yield next(list1)


    while True:
        if value1.percent <= value2.percent:
            # Yield the lower value.
            yield value1
            try:
                # Grab the next value from list1.
                value1 = next(list1)
            except StopIteration:
                # list1 is empty.  Yield the last value we received from list2, then
                # yield the rest of list2.
                yield value2
                while True:
                    yield next(list2)
        else:
            yield value2
            try:
                value2 = next(list2)

            except StopIteration:
                # list2 is empty.
                yield value1
                while True:
                    yield next(list1)
