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
# 8:00 - 12:00
MORNING_INDEXES = [0,1,2,3,4,5,6,7]

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
            day_array = getattr(self, s.day)
            day_array.append(s)

        self.matching_slots_each_day = {}

    def get_slots_count(self):
        count = 0
        for d in DAYS:
            day_list = getattr(self, d)
            count += len(day_list)

        return count

    def equal_check(self, x, s):
        return x.slot_index == s.slot_index and x.room == s.room

    def remove_slots(self, slots):
        for s in slots:
            days_slots = getattr(self, s.day)
            remove_slot_ind = [i for i, x in enumerate(days_slots) if self.equal_check(x, s)]
            del days_slots[remove_slot_ind[0]]

    # Gets a possible free slot for the course
    def get_free_slot(self, course):
        needed_slots = course.get_needed_slots()
        course_days = course.get_days()

        # Check for matching slots in each day, set all to []
        for d in DAYS:
            self.matching_slots_each_day[d] = []


        # Find valid slots for each day
        for ind, day in enumerate(course_days):
            for slot in getattr(self, day):
                # Requirments screening!!
                # Check if capacity matches
                if int(slot.room.capacity) >= int(course.students_per_section):
                    self.matching_slots_each_day[day].append(slot)

        # -- At this point we have all the available slots placed in each day array

        # Check if slots for each course day is potentially available
        bool_course_days_matched = True
        for day in course_days:
            if not len(self.matching_slots_each_day[day]):
                bool_course_days_matched = False
        if not bool_course_days_matched:
            # There are no slots for the days needed, so we can assign it
            return []

        # Get all_valid_slots in one list for grouping
        all_valid_slots = []
        for k, v in self.matching_slots_each_day.items():
            if v:
                all_valid_slots = all_valid_slots + v

        # -- At this point we have all the slots for the course days

        # Group the slots together by room
        room_groupings = {}
        for key, valuesiter in groupby(all_valid_slots, key=lambda s: s.room):
            if key.room in room_groupings.keys():
                room_groupings[key.room] = room_groupings[key.room] + list(v for v in valuesiter)
            else:
                room_groupings[key.room] = list(v for v in valuesiter)

        # Add grouping in each room by time
        room_time_grouping = {}
        for room, slots in room_groupings.items():
            slots.sort(key=lambda s: s.slot_index)
            room_time_grouping[room] = {}

            slots_grouping = []
            for key, valuesiter in groupby(slots, key=lambda s: s.slot_index):
                room_time_grouping[room][key] = list(v for v in valuesiter)

        # -- At this point we have each room keyed with the time slots grouped
        # -- by the time they are at

        # Now remove the slot groups that dont have the number of days needed
        # for the course. E.g. Remove groups of 1, when the course needs 2
        for room, groupings in room_time_grouping.items():
            remove_keys = []
            for group_key, group_slots in groupings.items():
                if len(group_slots) < len(course_days):
                    remove_keys.append(group_key)
            for k in remove_keys:
                del groupings[k]

        # Preferences screening!!
        # ?

        # -- At this point we have each room keyed with slot groupings by time
        # -- and together with matching days needed for the course

        # Pick a slot from free slots randomly
        # Count how many times we check for a free slot, end after checking all
        room_count = len(room_time_grouping.keys())  # All the room keys
        room_stop_at_zero = room_count  # Keep count to know when we have tried all the rooms
        slot_works = False  # Use to break out when success

        # Start with random room
        rooms = list(room_time_grouping.keys())
        rand_room_index = randint(0, room_count - 1)

        free_slots = []

        while not slot_works and room_stop_at_zero > 0:
            rand_room = rooms[rand_room_index]
            # print('------ROOM Check', rand_room)
            active_room = room_time_grouping[rand_room]

            # Given the room, see if slots work
            slot_count = len(active_room.keys())  # All the room keys
            slot_stop_at_zero = slot_count  # Keep count to know when we have tried all the slots

            # Start with random free slot
            slot = list(active_room.keys())
            rand_slot_index = 0 if len(slot) is 0 else randint(0, len(slot) - 1)

            while not slot_works and slot_stop_at_zero > 0:
                rand_slot = slot[rand_slot_index]
                active_slot = active_room[rand_slot]

                # Is there enough continuous time? Get the timeindex and check if
                # there are enough after it to fit the class into
                # E.g. Slot 2= 8:30, 2 hours class needs slots, 3,4,5,6,7

                bool_enough_time = True
                # Reset free slots if it didnt work out
                free_slots = []
                for n in range(needed_slots):
                    next_time = active_slot[0].slot_index + n
                    if next_time in slot:
                        free_slots = free_slots + active_room[next_time]
                    else:
                        bool_enough_time = False

                # If the slot works, save it
                if bool_enough_time:
                    slot_works = True

                # Go to the next slot, reset to 0 when at the end
                rand_slot_index = rand_slot_index + 1 if rand_slot_index + 1 < slot_count else 0
                slot_stop_at_zero -= 1
                # END SLOT LOOP

            # Go to the next room, reset to 0 when at the end
            rand_room_index = rand_room_index + 1 if rand_room_index + 1 < room_count else 0
            room_stop_at_zero -= 1

        self.remove_slots(free_slots)

        return free_slots


def create_slots(room):
    ROOM_SLOTS = []
    for ind, time in enumerate(TIMES):
        for day in DAYS:
            rs = TimeSlot(room, day, time, ind)
            ROOM_SLOTS.append(rs)

    return ROOM_SLOTS
