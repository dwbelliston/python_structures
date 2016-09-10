#!/usr/local/bin/python3
import os
import sys
import argparse


def main(arguments):

    parser = argparse.ArgumentParser(
        description='Receive Number and run factorial',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '-n', '--number', type=int, help="Number to run factorial on")
    args = parser.parse_args(arguments)

    number = args.number
    product = 1

    def factorial(n):
        nonlocal product
        if n > 0:
            product = product * n
            n -= 1
            factorial(n)

    factorial(number)
    print('Factorial of {} is {}'.format(number, product))


if __name__ == '__main__':
    main(sys.argv[1:])
