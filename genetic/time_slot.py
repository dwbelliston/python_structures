#!/usr/bin/env python3
class TimeSlot(object):
    def __init__(self, room, day, time_slot):
        self.room = room
        self.day = day
        self.time_slot = time_slot

    def get_value(self, key):
        return self[key]

    def __str__(self):
        return ('{}-{}-{}'.format(self.room.room, self.day, self.time_slot))

TIMES = [
        '8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30',
        '12:00', '12:30', '1:00', '1:30', '2:00', '2:30', '3:00', '3:30',
        '4:00', '4:30'
        ]

DAYS = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']


def create_slots(room):
    ROOM_SLOTS = []
    for time in TIMES:
        for day in DAYS:
            rs = TimeSlot(room, day, time)
            ROOM_SLOTS.append(rs)

    return ROOM_SLOTS
