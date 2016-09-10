#!/usr/bin/env python

import os
import sys
import argparse


def main(arguments):

    parser = argparse.ArgumentParser(
        description='Python Template',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '-i', '--infile', help="Input file",
        type=argparse.FileType('r'))
    parser.add_argument(
        '-o', '--outfile', help="Output file",
        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    print args

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
