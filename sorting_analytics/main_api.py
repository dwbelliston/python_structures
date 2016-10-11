#!/usr/bin/env python3
import copy
import time

from sorters.bubble import bubble_sort
from sorters.insertion import insertion_sort
from sorters.selection import selection_sort
from sorters.native_sort import native_sort
from sorters.quick_sort import quick_sort

FILENAMES = [
    # [ 'list1.txt', 'int'  ],
    # [ 'list2.txt', 'int'  ],
    # [ 'list3.txt', 'int'  ],
    # [ 'list4.txt', 'int'  ],
    # [ 'list5.txt', 'float'],
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
    def __init__(self, name, duration, nums):
        self.name = name
        self.duration = duration
        self.nums = nums
        self.relative = None

    def __str__(self):
        return '{}/{}'.format(self.name, self.duration)


def main():
    sort_broker = SortBroker()

    for file_info in FILENAMES:
        # Print the name of the list
        print(file_info[0])
        with open ('lists_bank/{}'.format(file_info[0]), "r") as f:
            results_all = []
        # For each of the six sorting algorithms, do the following:
            for i in SORTNAMES:
                sort_to_call = getattr(sort_broker, i)
                # Read the list into a list/array
                list_data=f.read().split()
                # Copy the list of numbers 1,000 times so you can sort more than once
                list_datum = [list_data for j in range(1000)]
                # Save the current time in millis
                start_time = int(round(time.time() * 1000))
                # In a for loop, sort each of the lists using the specific algorithm
                for l in list_datum:
                    sort_to_call(l)
                # Calculate the current time in millis minus the start time
                duration_time = int(round(time.time() * 1000) - start_time)
                # Create a `Result` object for this result
                # # You should now have five result objects: one for each algorithm.
                result = Result(i, duration_time, 0)
                results_all.append(result)

            # Determine which was the fastest, and calculate the relative increase in time of each algorithm.
            for i in results_all:
                print(i)
            # # The formula is: `100.0 * (algorithm time - fastest time) / fastest time`.
            # Sort the five results from fastest to slowest.
            # Print the times to the console as shown in `example_output.txt`.  Please try to match this file exactly with your output.  The relative time is rounded to the nearest integer.  Note that the first 10 and last 10 numbers of each set are included in the printout.
            # sort_me(list_data)


### Main runner ###
if __name__ == '__main__':
    main()
