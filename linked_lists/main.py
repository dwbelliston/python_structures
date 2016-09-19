#!/usr/bin/env python3
import os
import csv
import sys
import argparse
from linked_api import LinkedList


def main(arguments):
    parser = argparse.ArgumentParser(description='Linked List methods')
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'), help="File with instruction set")
    args = parser.parse_args(arguments)

    # instruction_set map
    instruction_map = {}

    # Step through the instruction set one at a time
    count = 0
    with open('output.txt', 'w') as file_write:
        with args.file as f:
            instruction_set = csv.reader(f)
            for instruction in iter(instruction_set):
                ins_func = instruction[0].lower()
                file_write.writelines('{}: {}\n'.format(count, instruction))
                if ins_func == 'create':
                    linked_list = LinkedList(file_write)
                elif ins_func == 'debug':
                    linked_list.debug_print()
                elif ins_func == 'add':
                    linked_list.add(instruction[1])
                else:
                    # Get, Set, Insert, Swap, Delete
                    methodToCall = getattr(linked_list, ins_func)
                    if instruction[2]:
                        methodToCall(instruction[1], instruction[2])
                    else:
                        methodToCall(instruction[1])
                count += 1

if __name__ == '__main__':
    main(sys.argv[1:])
