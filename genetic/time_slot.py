#!/usr/bin/env python3
from random import randint
from itertools import groupby
from operator import itemgetter
from pprint import pprint

# Mon-Fri for possible classes
NUM_DAYS = 5

TIMES = [
        '8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30',
        '12:00', '12:30', '1:00', '1:30', '2:00', '2:30', '3:00', '3:30',
        '4:00', '4:30'
        ]

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']


class TimeSlot(object):
    def __init__(self, room, day, time_slot, slot_index):
        self.room = room
        self.day = day
        self.time_slot = time_slot
        self.slot_index = slot_index

    def get_value(self, key):
        return self[key]

    def __str__(self):
        return ('{}-{}-{}'.format(self.room.room, self.day, self.time_slot))


class AllSlots(object):
    def __init__(self, slots):
        for d in DAYS:
            setattr(self, d, [])

        # split the slots into day lists
        for s in slots:
            v = getattr(self, s.day)
            v.append(s)

        self.matching_slots_each_day = {}

    def get_slots_count(self):
        count = 0
        for d in DAYS:
            day_list = getattr(self, d)
            count += len(day_list)

        return count

    # Gets a possible free slot for the course
    def get_free_slot(self, course):
        needed_slots = course.get_needed_slots()
        course_days = course.get_days()

        # Check for matching slots in each day
        for d in DAYS:
            self.matching_slots_each_day[d] = []

        # Find valid slots for each day
        for ind, day in enumerate(course_days):
            for slot in getattr(self, day):
                # Requirments screening!!
                # Check if capacity matches
                if slot.room.capacity >= course.students_per_section:
                    self.matching_slots_each_day[day].append(slot)

        # Check if matching_slots for each course day, if not return no matches
        bool_course_days_matched = True
        for day in course_days:
            if not len(self.matching_slots_each_day[day]):
                bool_course_days_matched = False
        if not bool_course_days_matched:
            return []

        all_valid_slots = []
        for k, v in self.matching_slots_each_day.items():
            if v:
                all_valid_slots = all_valid_slots + v

        room_groupings = {}
        for key, valuesiter in groupby(all_valid_slots, key=lambda s: s.room):
            if key.room in room_groupings.keys():
                room_groupings[key.room] = room_groupings[key.room] + list(v for v in valuesiter)
            else:
                room_groupings[key.room] = list(v for v in valuesiter)

        room_time_grouping = {}
        for room, slots in room_groupings.items():
            slots.sort(key=lambda s: s.slot_index)
            room_time_grouping[room] = {}

            slots_grouping = []
            for key, valuesiter in groupby(slots, key=lambda s: s.time_slot):
                room_time_grouping[room][key] = list(v for v in valuesiter)

        pprint(room_time_grouping)



        slots_groupings = []
        # for key, valuesiter in groupby(sorted_valid_slots, key=lambda s: s.room):
        #     print(key, [v for v in valuesiter])
            # slots_groupings.append(dict(time_slot=key, items=list(v for v in valuesiter)))

        # for r in slots_groupings:
        #     print('-----')
        #     for k in r['items']:
        #         print(k)

        # Preferences screening!!
        # ?

        # Count how many times we check for a free slot, end after checking all
        stop_at_zero = len(slots_groupings)

        free_slots = []
        # # Start somewhere random
        # active_index = randint(0, all_slots_count - 1)
        #
        # while not free_slot and stop_at_zero > 0:
        #     # See if course matches
        #     test_slot = self.slots[active_index]
        #
        #     # Go to the next slot, reset to 0 when at the end
        #     active_index = active_index + 1 if active_index + 1 < all_slots_count else 0
        #     stop_at_zero -= 1

        return free_slots



def create_slots(room):
    ROOM_SLOTS = []
    for ind, time in enumerate(TIMES):
        for day in DAYS:
            rs = TimeSlot(room, day, time, ind)
            ROOM_SLOTS.append(rs)

    return ROOM_SLOTS
