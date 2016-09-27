#!/usr/bin/env python3

class DoublyLinkedList(object):
    '''
    A doubly-linked list implementation that holds arbitrary objects.
    '''

    def __init__(self, file_write):
        '''Creates a linked list.'''
        self.size = 0
        self.head = Node(None)
        self.file_write = file_write

    def _set_head(self, new_head):
        self.head = new_head

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

        content_rev = ', '.join(str(x) for x in reverse_gen(content))
        content_for = ', '.join(str(x) for x in content)
        print('{} >>> {} >>> {}'.format(self.size, content_rev, content_for))
        self.file_write.writelines('{} >>> {} >>> {}\n'.format(self.size, content_rev, content_for))


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
            self.head._set_prev(new_node)

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
            new_node._set_next(insert_node.get_next())
            new_node._set_prev(insert_node)
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
                delete_node_forward._set_next(delete_node.get_next())
            else:
                self.head = delete_node.get_next()
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
        self.prev = None
        self.next = None

    def _set_next(self, next):
        self.next = next

    def _set_prev(self, prev):
        self.prev = prev

    def _set_value(self, item):
        self.value = item

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def __str__(self):
        return '<Node: {}>'.format(self.value)


# #######
def reverse_gen(arr):
    for i in reversed(arr):
        yield i
