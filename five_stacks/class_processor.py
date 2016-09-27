#!/usr/bin/env python3
from api_circularlist import CircularLinkedList, CircularLinkedListIterator
from api_doublylinked import DoublyLinkedList
from api_stack import Stack
from api_queue import Queue

class Processor(object):

    def __init__(self, output_file):
        '''Creates the lists'''
        self.callahead = DoublyLinkedList(output_file)
        self.waiting = DoublyLinkedList(output_file)
        self.appetizers = Queue(output_file)
        self.buzzers = Stack(output_file)
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.songs = CircularLinkedList()
        self.songs.add('Song 1')
        self.songs.add('Song 2')
        self.songs.add('Song 3')
        self.songs_iter = CircularLinkedListIterator(self.songs)

    def run(self, instruction_file):
        '''Processes the given file stream.'''
        for line_i, line in enumerate(instruction_file):
            line = line.rstrip()
            # split and handle the commands here
            # print(line)

        self.callahead.add('1')
        self.callahead.add('2')
        self.callahead.add('3')
        self.callahead.insert(0, 'a')
        self.callahead.insert(1, 'b')
        self.callahead.debug_print()
        self.callahead.swap(0, 4)
        self.callahead.swap(1, 3)
        self.callahead.delete(0)
        self.callahead.set(3, 'E')
        self.callahead.debug_print()


    def debug(self):
        self.callahead.debug_print()
        self.waiting.debug_print()
        self.appetizers.debug_print()
        self.buzzers.debug_print()
        self.songs.debug_print()
