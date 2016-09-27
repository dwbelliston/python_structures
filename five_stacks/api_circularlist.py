#!/usr/bin/env python3

class CircularLinkedList(object):
    '''
    A circularly-linked list implementation that holds arbitrary objects.
    '''

    def __init__(self, file_write):
        '''Creates a linked list.'''
        self.size = 0
        self.head = Node(None)
        self.file_write = file_write

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
        cycle_count = 0
        while current and cycle_count < self.size:
            content.append(current.value)
            current = current.get_next()
            cycle_count += 1

        content = ', '.join(str(x) for x in reverse_gen(content))
        print('{} >>> {}'.format(self.size, content))
        self.file_write.writelines('{} >>> {}\n'.format(self.size, content))

        print('-----')
        print(self.head)
        print(self.head.next)
        print(self.head.next.next)
        print(self.head.next.next.next)
        print(self.head.next.next.next.next)
        print(self.head.next.next.next.next.next)
        print(self.head.next.next.next.next.next.next)
        print(self.head.next.next.next.next.next.next.next)
        print(self.head.next.next.next.next.next.next.next.next)
        print(self.head.next.next.next.next.next.next.next.next.next)
        print(self.head.next.next.next.next.next.next.next.next.next.next)
        print(self.head.next.next.next.next.next.next.next.next.next.next.next)



    def debug_cycle(self, count):
        '''Prints a representation of the entire cycled list up to count items'''
        content = []
        current = self.head
        cycle_count = 0
        while current and cycle_count <= count:
            content.append(current.value)
            current = current.get_next()
            cycle_count += 1

        content = ', '.join(str(x) for x in reverse_gen(content))
        print('{} >>> {}'.format(self.size, content))
        self.file_write.writelines('{} >>> {}\n'.format(self.size, content))


    def _get_index(self, index):
        # If index is equal or greater than size OOB
        goal_index = self.size - index

        if self.size != 0:
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
            print('Error: Index {} out of bounds\n'.format(index))
            self.file_write.writelines('Error: Index {} out of bounds\n'.format(index))
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
            new_node._set_next(self.head)
            self._get_node(0)._set_next(new_node)

        # Move the head forward to the new node
        self._set_head(new_node)
        # Increase the size of the new node
        self._increase_size()


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        index = int(index)

        new_node = Node(item)
        insert_node = self._get_node(index)
        if insert_node:
            new_node._set_next(insert_node.next)
            insert_node._set_next(new_node)
            self._increase_size()



    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        index = int(index)
        set_node = self._get_node(index)
        if set_node:
            set_node._set_value(item)


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        index = int(index)

        get_node = self._get_node(index)
        if get_node:
            self.file_write.writelines(get_node.value + '\n')
            return get_node


    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        index = int(index)
        delete_node = self._get_node(index)
        if delete_node:
            delete_node_forward = self._get_node(index + 1)
            if delete_node_forward:
                delete_node_forward._set_next(delete_node.next)
            else:
                self.head = delete_node.next
                self.head.next = self._get_node(0)
            self._decrease_size()



    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        index1, index2 = int(index1), int(index2)

        node_1 = self._get_node(index1)
        node_2 = self._get_node(index2)

        if node_1 and node_2:
            node_1.value, node_2.value = node_2.value, node_1.value



######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def _set_next(self, next):
        self.next = next

    def _set_value(self, item):
        self.value = item

    def get_next(self):
        return self.next

    def __str__(self):
        return '<Node: {}>'.format(self.value)


######################################################
###   An iterator for the circular list

class CircularLinkedListIterator(object):
    def __init__(self, circular_list):
        '''Starts the iterator on the given circular list.'''
        self.list = circular_list
        self.position = 0

    def _has_next(self):
        '''Returns whether there is another value in the list.'''
        return True if self.list.size > self.position else False

    def next(self):
        '''Returns the next value, and increments the iterator by one value.'''
        has_next = self._has_next()
        if has_next:
            next_song = self.list._get_node(self.position)
            self.position += 1
        else:
            next_song = self.list._get_node(0)
            self.position = 1
        return next_song


def reverse_gen(arr):
    for i in reversed(arr):
        yield i
