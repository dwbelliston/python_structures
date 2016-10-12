#!/usr/bin/env python3
import copy
import time

from sorters.bubble_obj_sort import bubble_obj_sort

from sorters.bubble import bubble_sort
from sorters.insertion import insertion_sort
from sorters.selection import selection_sort
from sorters.native_sort import native_sort
from sorters.quick_sort import quick_sort

FILENAMES = [
    [ 'list1.txt', 'int'  ],
    [ 'list2.txt', 'int'  ],
    [ 'list3.txt', 'int'  ],
    [ 'list4.txt', 'int'  ],
    [ 'list5.txt', 'float'],
    [ 'list6.txt', 'int'  ],
]

SORTNAMES = ['bubble', 'native', 'quick', 'insertion', 'selection']


class SortBroker(object):
    def bubble(self, list):
        bubble_sort(list)

    def native(self, list):
        native_sort(list)

    def selection(self, list):
        selection_sort(list)

    def insertion(self, list):
        insertion_sort(list)

    def quick(self, list):
        quick_sort(list)



class Result:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.last_nums = None
        self.right_nums = None
        self.relative = None

    def __str__(self):
        return '{}/{}'.format(self.name, self.duration)


def main():
    sort_broker = SortBroker()
    fastest_alg = Result('Void', 0)

    for file_info in FILENAMES:
        # Print the name of the list
        print(file_info[0])
        results_all = []
        with open ('lists_bank/{}'.format(file_info[0]), "r") as f:
            list_data=f.read().split()

        # For each of the six sorting algorithms, do the following:
        for i in SORTNAMES:
            sort_to_call = getattr(sort_broker, i)
            # Read the list into a list/array
            # Copy the list of numbers 1,000 times so you can sort more than once
            list_datum = [list_data for j in range(1000)]

            # Save the current time in millis
            start_time = time.time() * 1000

            # In a for loop, sort each of the lists using the specific algorithm
            for l in list_datum:
                sort_to_call(l)

            # Calculate the current time in millis minus the start time
            duration_time = round((time.time() * 1000 - start_time) / 1000, 6)

            # Create a `Result` object for this result
            # # You should now have five result objects: one for each algorithm.
            result = Result(i, duration_time)
            results_all.append(result)

            # Determine which was the fastest
            if result.duration < fastest_alg.duration or fastest_alg.name == 'Void':
                fastest_alg = result

            # get first and last 10
            result.first_nums = list_datum[0][:10]
            result.last_nums = list_datum[0][-10:]

        # Calculate the relative increase in time of each algorithm.
        for i in results_all:
            # # The formula is: `100.0 * (algorithm time - fastest time) / fastest time`.
            i.relative = (i.duration - fastest_alg.duration) / fastest_alg.duration
            i.relative = round(i.relative * 100.0)

        # Sort the five results from fastest to slowest.
        results_all = bubble_obj_sort(results_all, [{'name': 'duration', 'dir': 'asc'}])

        # Print the times to the console as shown in `example_output.txt`.  Please try to match this file exactly with your output.  The relative time is rounded to the nearest integer.  Note that the first 10 and last 10 numbers of each set are included in the printout.
        for i in results_all:
            print('{} Sort'.format(i.name.capitalize()))
            print('{}'.format(i.duration))
            print('{}%'.format(i.relative))
            print('First 10: {}'.format(', '.join([x for x in i.first_nums])))
            print('Last 10: {}'.format(', '.join([x for x in i.last_nums])))
            print('\n')


### Main runner ###
if __name__ == '__main__':
    main()
