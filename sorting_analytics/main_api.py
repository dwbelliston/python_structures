#!/usr/bin/env python3
import copy

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


class Result:
    def __init__(self, name, duration, nums):
        self.name = name
        self.duration = duration
        self.nums = nums
        self.relative = None


def sort_me(list_data):
    list_bubbled = bubble_sort(copy.copy(list_data))
    list_selection = selection_sort(copy.copy(list_data))
    list_insertion = insertion_sort(copy.copy(list_data))
    list_quick = quick_sort(copy.copy(list_data))
    list_native = native_sort(copy.copy(list_data))
    print(list_bubbled == list_selection == list_insertion == list_quick == list_native)


def main():
    for file_info in FILENAMES:
        with open ('lists_bank/{}'.format(file_info[0]), "r") as f:
            list_data=f.read().split()
            sort_me(list_data)


### Main runner ###
if __name__ == '__main__':
    main()
