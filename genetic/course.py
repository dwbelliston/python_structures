#!/usr/bin/env python3
class Course(object):
    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key.lower().replace(" ", "_"), value)

    def get_value(self, key):
        return self[key]

    def __str__(self):
        return ('{}:[{}]'.format(self.course, self.section))
