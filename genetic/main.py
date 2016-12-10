#!/usr/bin/env python3
import os
import sys
import argparse
import re
import csv
from course import Course
from room import Room
from time_slot import create_slots

# 'course', 'friday', 'get_value', 'hours', 'monday', 'preferred_room_type', 'preferred_time', 'section', 'students_per_section', 'thursday', 'tuesday', 'wednesday'


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
    # Available times for each room in 30 min increment
    with open('rooms.csv', newline='') as f:
        reader = csv.reader(f)
        keys = next(reader)
        for row in reader:
            r = Room(dict(zip(keys, row)))
            ROOMS.append(r)
            time_slots = create_slots(r)
            TIMESLOTS = TIMESLOTS + time_slots


    # Randomly get a class and assign it

    # Collection of all the classes to rooms is a solution


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
