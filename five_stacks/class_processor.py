#!/usr/bin/env python3
from api_circularlist import CircularLinkedList, CircularLinkedListIterator
from api_doublylinked import DoublyLinkedList
from api_stack import Stack
from api_queue import Queue
import csv

class Processor(object):

    def __init__(self, output_file):
        '''Creates the lists'''
        self.file_write = output_file

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
        self.songs = CircularLinkedList(output_file)
        self.songs.add('Song 1')
        self.songs.add('Song 2')
        self.songs.add('Song 3')
        self.songs_iter = CircularLinkedListIterator(self.songs, output_file)

    def run(self, instruction_file):
        '''Processes the given file stream.'''
        instruction_set = csv.reader(instruction_file)

        # Step through the instruction set one at a time
        count = 0
        for instruction in iter(instruction_set):
            if count < 100:
                ins_func = instruction[0].lower()

                print('{}: {}'.format(count, instruction))
                self.file_write.writelines('{}: {}\n'.format(count, instruction))

                # Map the ins_func to the method and invoke
                getattr(self, 'run_{}'.format(ins_func))(*instruction)

                count += 1

    def run_debug(self, *args):
        self.debug()

    def run_song(self, *args):
        self.songs_iter.next()

    def run_appetizer(self, *args):
        appetizer_name = self.appetizers.dequeue()
        waiters = []
        count = 0
        next_waiting = self.waiting.head
        while next_waiting and count < 3:
            waiters.append(next_waiting.value)
            next_waiting = next_waiting.next
            count += 1
        waiters = ', '.join(str(x) for x in waiters)
        print('{} >>> {}'.format(appetizer_name, waiters))

    def run_appetizer_ready(self, *args):
        self.appetizers.enqueue(args[1])

    def run_call(self, *args):
        self.callahead.add(args[1])

    def run_arrive(self, *args):
        # If they are arriving, but already in the waiting, then they called ahead
        guest = args[1]
        is_callahead = False
        next_callahead = self.callahead.head

        while next_callahead:
            if next_callahead.value == guest:
                is_callahead = True
            next_callahead = next_callahead.next

        if is_callahead:
            insert_callahead = 0 if self.waiting.size < 5 else self.waiting.size - 5
            self.waiting.insert(insert_callahead, guest)
            callahead_index = self.callahead._search_node(guest)
            self.callahead.delete(callahead_index - 1)

        else:
            self.waiting.add(args[1])

        self.buzzers.pop()

    def run_seat(self, *args):
        seat_guest = self.waiting._get_node(0)
        self.waiting.delete(0)
        self.buzzers.push('Buzzer')
        if seat_guest:
            self.file_write.writelines('{}\n'.format(seat_guest.value))
            print(seat_guest.value)


    def run_leave(self, *args):
        delete_index = self.waiting._search_node(args[1])
        self.waiting.delete(delete_index)
        self.buzzers.push('Buzzer')

    def debug(self):
        self.callahead.debug_print()
        self.waiting.debug_print()
        self.appetizers.debug_print()
        self.buzzers.debug_print()
        self.songs.debug_print()
