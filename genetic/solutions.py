from time_slot import AllSlots
from random import randint


#!/usr/bin/env python3
class Solution(object):
    def __init__(self):
        pass

    # getFitness(): Calculates the fitness function for the current time slot.
    def getFitness(self):
        print('Get Fitness of the solution')

    # crossover(other): Crosses with another solution and returns a new solution.
    # mutate(): Mutates the solution in some way.
    def __str__(self):
        self


class CourseAssignment(object):
    def __init__(self, course, time, room):
        self.course = course
        self.time = time
        self.room = room

    def get_fitness():
        print('Get ind fitness')


def create_solution(TIMESLOTS, COURSES, run, generation):
    slots_pool = AllSlots(TIMESLOTS)

    while len(COURSES):
        active_course = COURSES[randint(0, len(COURSES)-1)]
        time = slots_pool.get_free_slot(active_course)

        # assignment = CourseAssignment(active_course, time, room)
        COURSES.pop()
