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
        self.file_write = file_write


    def debug_print(self):
        '''Prints a representation of the entire queue.'''


    def enqueue(self, item):
        '''Adds an item to the end of the queue'''


    def dequeue(self):
        '''
        Dequeues the first item from the list.  This involves the following:
            1. Get the first node in the list.
            2. Delete the node from the list.
            3. Return the value of the node.
        '''

    def size(self):
        '''Returns the number of items in the queue'''
