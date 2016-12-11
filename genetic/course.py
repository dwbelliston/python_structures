#!/usr/bin/env python3
class Course(object):
    # 'course', 'friday', 'get_value', 'hours', 'monday', 'preferred_room_type', 'preferred_time', 'section', 'students_per_section', 'thursday', 'tuesday', 'wednesday'
    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key.lower().replace(" ", "_"), value)

    def get_value(self, key):
        return self[key]

    def get_needed_slots(self):
        return round((float(self.hours)+.25)/.5 + .1)

    def get_days(self):
        DAYS = ['friday', 'monday', 'thursday', 'tuesday', 'wednesday']
        course_days = []
        for k in DAYS:
            value = getattr(self, k.lower())
            if value == 'x':
                course_days.append(k)

        return course_days

    def __str__(self):
        return ('{}:[{}]'.format(self.course, self.section))
