#!/usr/bin/env python3
class BNode(object):
    '''
    binary tree node
    '''

    '''When the tree is modified (`set`, `remove`), be sure to update the
    `parent`, `left`, and `right` references.'''

    def __init__(self, key, value, parent=None, left=None, right=None):
        '''A node in the BTree'''

        self.key = key
        self.value = value
        # a reference to the parent of the node.
        self.parent = parent
        # a reference to the left child of the node.
        self.left = left
        # a reference to the right child of the node.
        self.right = right

    def has_left(self):
        return True if self.left else False

    def has_right(self):
        return True if self.right else False

    def __str__(self):
        # key(parentkey)
        if self.parent:
            return '{}({})'.format(self.key, self.parent.key)
        else:
            return '{}(-)'.format(self.key)
