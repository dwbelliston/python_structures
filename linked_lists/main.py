#!/usr/bin/env python3
import os
import csv
import sys
import argparse
from linked_api import LinkedList


def main(arguments):
    parser = argparse.ArgumentParser(description='Array methods')
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'), help="File with instruction set")
    args = parser.parse_args(arguments)

    linked_list = LinkedList()
    linked_list.add('a')
    linked_list.add('b')
    linked_list.add('c')
    linked_list.add('d')
    linked_list.add('e')
    linked_list.debug_print()
    linked_list.set(0, 'A')
    linked_list.set(4, 'E')
    linked_list.debug_print()

if __name__ == '__main__':
    main(sys.argv[1:])
