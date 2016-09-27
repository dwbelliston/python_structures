#!/usr/bin/env python3
from api_linkedlist import LinkedList

class Queue(object):
    '''
    A linked list implementation of a queue.

    This contains a LinkedList internally.  It does not extend LinkedList.
    In other words, this class uses "Composition" rather than "Inheritance".
    '''

    def __init__(self, file_write):
        '''Constructor'''
        self.list = LinkedList(file_write)

    def debug_print(self):
        '''Prints a representation of the entire queue.'''
        self.list.debug_print()

    def enqueue(self, item):
        '''Adds an item to the end of the queue'''
        self.list.add(item)

    def dequeue(self):
        '''
        Dequeues the first item from the list.  This involves the following:
            1. Get the first node in the list.
            2. Delete the node from the list.
            3. Return the value of the node.
        '''
        if self.size() > 0:
            next_node = self.list._get_node(0)
            self.list.delete(0)
            return next_node.value
        else:
            print('Error: Queue is empty')

    def size(self):
        '''Returns the number of items in the queue'''
        return self.list.size
