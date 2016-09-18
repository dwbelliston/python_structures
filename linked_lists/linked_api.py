#!/usr/bin/env python3
class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.size = 0
        self.head = Node(None)

    def _set_head(self, head):
        self.head = head

    def _increase_size(self):
        self.size += 1

    def _decrease_size(self):
        self.size -= 1

    def debug_print(self):
        '''Prints a representation of the entire list.'''
        content = []
        current = self.head
        while current:
            content.append(current.value)
            current = current.get_next()

        content = ', '.join(str(x) for x in reverse_gen(content))
        print('{} >>> {}'.format(self.size, content))

    def _get_index(self, index):
        # If index is equal or greater than size OOB
        goal_index = self.size - index
        goal_index -= 1
        if goal_index < 0:
            raise IndexError
        else:
            return goal_index


    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        # Get the target index, because its reversed
        try:
            goal_index = self._get_index(index)
        except IndexError:
            print('Error: Index {} out of bounds'.format(index))
            return None

        goal_node = None

        track_index = 0
        track_node = self.head

        while track_node:
            if track_index == goal_index:
                goal_node = track_node
                track_node = None
            else:
                track_node = track_node.get_next()
            track_index += 1

        return goal_node

    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        new_node = Node(item)

        # If the head is not the start, reference it
        if self.size > 0:
            new_node.set_next(self.head)

        # Move the head forward to the new node
        self._set_head(new_node)
        # Increase the size of the new node
        self._increase_size()


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        set_node = self._get_node(index)
        if set_node:
            set_node.set_value(item)


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''


    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''


    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''



######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next):
        self.next = next

    def set_value(self, item):
        self.value = item

    def get_next(self):
        return self.next

    def __str__(self):
        return '<Node: {}>'.format(self.value)


def reverse_gen(arr):
    for i in reversed(arr):
        yield i
