from time_slot import AllSlots, MORNING_INDEXES
from random import randint


#!/usr/bin/env python3
class Solution(object):
    def __init__(self, run, number, TIMESLOTS, COURSES):
        self.run = run
        self.number = number

        self.assignments = []
        self.unassigned = []

        self.slots_pool = AllSlots(TIMESLOTS)
        self.start_slots_pool_count = len(TIMESLOTS)

        self.courses_pool = COURSES
        self.start_course_count = len(COURSES)
        

    # getFitness(): Calculates the fitness function for the current time slot.
    def get_fitness(self):
        # SolutionFitValue = 0.6 * avg_ind_fitness  +  0.2 * FreeTimeBlocks  -  0.2 * StudentsOutsideTNRB  +  0.2 * UnusedRooms
        sum_ind_fitness = 0
        for assignment in self.assignments:
            sum_ind_fitness += assignment.fitness

        avg_ind_fitness = sum_ind_fitness / self.start_course_count
        free_time_blocks = 100 * self.slots_pool.get_slots_count() / self.start_slots_pool_count

        students_unassigned = 0
        for c in self.unassigned:
            students_unassigned += int(c.students_per_section)
        students_outside_trnb = 100 * students_unassigned / 6277

        # TODO: Calculate this, would have to iterate over the timeslots to do it
        unused_rooms = 100 * 5 / 32

        return (0.6 * avg_ind_fitness) + (0.2 * free_time_blocks) - (0.2 * students_outside_trnb) + (0.2 * unused_rooms)

    # crossover(other): Crosses with another solution and returns a new solution.
    # mutate(): Mutates the solution in some way.
    def __str__(self):
        return '{}.{}'.format(self.run['index'], self.number)

    def create_solution(self):
        while len(self.courses_pool):
            rand_ind = randint(0, len(self.courses_pool)-1)
            active_course = self.courses_pool[rand_ind]
            time_slots = self.slots_pool.get_free_slot(active_course)
            if len(time_slots):
                assignment = CourseAssignment(active_course, time_slots)
                self.assignments.append(assignment)
            else:
                self.unassigned.append(active_course)
            self.courses_pool.pop(rand_ind)


class CourseAssignment(object):
    def __init__(self, course, time_slots):
        self.course = course
        self.time_slots = time_slots
        self.fitness = self.get_fitness()

    # IndvFitness = CapacityValue + PrefTime + PrefRoomType
    def get_fitness(self):
        room_capacity = int(self.time_slots[0].room.capacity)
        course_capacity = int(self.course.students_per_section)
        net_capacity = room_capacity - course_capacity

        # Capacity Fitness
        if net_capacity <= 5:
            capacity_value = 50
        elif net_capacity <= 10:
            capacity_value = 40
        elif net_capacity <= 15:
            capacity_value = 30
        elif net_capacity <= 20:
            capacity_value = 20
        elif net_capacity <= 25:
            capacity_value = 10
        else:
            capacity_value = 0

        # PrefTime fitness
        time_start = self.time_slots[0].slot_index
        time_end = self.time_slots[-1].slot_index

        if self.course.preferred_time == 'Morning':
            if time_start in MORNING_INDEXES:
                if time_end in MORNING_INDEXES:
                    pref_time_value = 25
                else:
                    pref_time_value = 15
            else:
                pref_time_value = 0
        # Afternoon
        else:
            if time_start not in MORNING_INDEXES:
                if time_end not in MORNING_INDEXES:
                    pref_time_value = 25
                else:
                    pref_time_value = 15
            else:
                pref_time_value = 0

        # Room fitness
        room_type = self.time_slots[0].room.type
        course_pref_room = self.course.preferred_room_type

        if course_pref_room == room_type or course_pref_room == 'None':
            room_type_value = 25
        else:
            room_type_value = 0

        return capacity_value + pref_time_value + room_type_value

    def __str__(self):
        return 'ASSIGNED:{}//{}'.format(self.course, [ts.__str__() for ts in self.time_slots])
