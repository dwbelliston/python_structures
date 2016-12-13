#!/usr/bin/env python3
import os
import sys
import argparse
import re
import csv
from course import Course
from room import Room
from time_slot import create_slots, AllSlots
from settings import RUNS
from solutions import Solution
import copy


def main(arguments):
    ROOMS = []
    TIMESLOTS = []
    COURSES = []

    # Create course objects for each section of each course
    with open('classes.csv', newline='') as f:
        reader = csv.reader(f)
        keys = next(reader)
        section_index = keys.index('Sections')
        keys[section_index] = 'Section'

        for row in reader:
            for section in range(1, int(row[section_index])+1):
                row[section_index] = section
                c = Course(dict(zip(keys, row)))
                COURSES.append(c)

    # Create room objects for each room
    with open('rooms.csv', newline='') as f:
        reader = csv.reader(f)
        keys = next(reader)
        for row in reader:
            r = Room(dict(zip(keys, row)))
            ROOMS.append(r)
            time_slots = create_slots(r)
            # Available times for each room in 30 min increment
            TIMESLOTS = TIMESLOTS + time_slots

    # Begin runs
    for run_ind, run in enumerate(RUNS):
        moving_average = 10
        run['index'] = run_ind + 1
        # Stop generations when moving average dips below 1
        while moving_average > 1.0:
            # create solutions
            for i in range(run['solutions']):
            # for i in range(1):
                course_copies = copy.deepcopy(COURSES)
                solution = Solution(run, i, TIMESLOTS, course_copies)
                solution.create_solution()
                a = solution.get_fitness()

                print(solution, a)
            moving_average = 0

    # Collection of all the classes to rooms is a solution


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
