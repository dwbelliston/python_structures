#!/usr/bin/env python3
import os
import sys
import argparse

from class_processor import Processor


def main(arguments):
    parser = argparse.ArgumentParser(description='Linked List methods')
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'),
        help="File with instruction set", required=True)
    parser.add_argument(
        '-o', '--output', type=argparse.FileType('w'),
        help="File to write to", default='output.txt')

    args = parser.parse_args(arguments)

    # Pass the output file
    processor = Processor(args.output)
    # Pass the instruction file
    processor.run(args.file)

if __name__ == '__main__':
    main(sys.argv[1:])
