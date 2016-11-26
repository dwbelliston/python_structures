#!/usr/bin/env python3
from queue import *


class BTree(object):
    '''
    binary tree class
    '''

    def __init__(self):
        '''Creates a tree with an intial size.'''
        # The tree has at least one field, `root`, that is the top node of tree
        self.root = None
        # self.size = 0

    def set(self, k, v):
        '''stores a key=value pair to the tree in the appropriate spot.'''
        if self.root:
            self._set(k, v, self.root)
        else:
            self.root = BNode(k, v)

    def _set(self, k, v, target_node):
        # Go down right side
        if v > target_node.value:
            if target_node.has_right():
                self._set(k, v, target_node.right)
            else:
                # Be first to the right
                target_node.right = BNode(k, v, target_node)

        # Go down left side
        if v < target_node.value:
            if target_node.has_left():
                self._set(k, v, target_node.left)
            else:
                # Be first to the left
                target_node.left = BNode(k, v, target_node)

    def get(self, key):
        '''returns the value stored with the given key.  If the key does not
        exist, null/None should be returned.'''
        node = self._find(key, self.root) if self.root else None
        return node.value if node else None

    def remove(self, key):
        '''removes the node with the given key from the tree.  If the key does
        not exist, it should simply return (no error).'''
        remove_node = self._find(key, self.root)

        # Leaf node, just delete
        if not remove_node.has_left() and not remove_node.has_right():
            self._remove_no_child(remove_node)

        else:
            # Node has two children, go left and find the highest replacement
            if remove_node.has_left() and remove_node.has_right():
                self._remove_two_child(remove_node)
            else:
                # Node has one child, replace it with the child node.
                self._remove_one_child(remove_node)

    def _remove_no_child(self, node):
        if node.parent.right == node:
            node.parent.right = None

        elif node.parent.left == node:
            node.parent.left = None

    def _remove_one_child(self, node):
        replacement_node = node.right if node.right else node.left

        if node.parent.right == node:
            replacement_node.parent = node.parent
            node.parent.right = replacement_node

        elif node.parent.left == node:
            replacement_node.parent = node.parent
            node.parent.left = replacement_node

    def _remove_two_child(self, node):
        largest_left = self._find_largest_left(node.left)

        # Remove the node from the tree
        self._remove_no_child(largest_left)

        # Change reference to parent
        largest_left.parent = node.parent

        #  Change reference on parent
        if node.parent.right == node:
            node.parent.right = largest_left
        else:
            node.parent.left = largest_left

        # Change reference on children
        node.left.parent = largest_left
        node.right.parent = largest_left

        # Change reference to left and right
        largest_left.left, largest_left.right = node.left, node.right

    def _find_largest_left(self, node):
        while node.right:
            node = node.right
        return node

    def print_values(self):
        self.walk_dfs_inorder(self.root)


    def walk_dfs_inorder(self, node):
        '''iterates through the nodes of the tree in depth-first-search
        "inorder" order.'''
        if node is not None:
            self.walk_dfs_inorder(node.left)
            print('{}, '.format(node.value), end='')
            self.walk_dfs_inorder(node.right)

    def walk_dfs_preorder(self, node):
        '''iterates through the nodes of the tree in depth-first-search
        "preorder" order.'''
        if node is not None:
            print(node.value)
            self.walk_dfs_preorder(node.left)
            self.walk_dfs_preorder(node.right)


    def walk_dfs_postorder(self, node):
        '''iterates through the nodes of the tree in depth-first-search
        "postorder" order.'''
        if node is not None:
            self.walk_dfs_postorder(node.left)
            self.walk_dfs_postorder(node.right)
            print(node.value)

    def walk_bfs(self):
        '''iterates through the nodes of the tree in breadth-first-search
        order.'''
        q = Queue()
        q.put(self.root)
        while not q.empty():
            c_node = q.get()
            print(c_node.value)
            if c_node.left is not None:
                q.put(c_node.left)
            if c_node.right is not None:
                q.put(c_node.right)

    def debug_print(self, q=None):
        '''prints a graphical representation of the tree. See below for more
        information.'''
        # Starting with the root
        if q is None:
            if self.root:
                next_q = Queue()
                next_q.put(self.root)
                self.debug_print(next_q)
            else:
                print('--')

        elif q.empty():
            # At the end of the levels
            print("")

        else:
            next_q = Queue()
            while not q.empty():
                next_node = q.get()
                print(next_node, end=" ")
                if next_node.has_left():
                    next_q.put(next_node.left)
                if next_node.has_right():
                    next_q.put(next_node.right)

            print("") # start the new line
            self.debug_print(next_q)


    def _replace_node(oldnode, newnode):
        '''replaces a node with another node in the tree.  This is useful when
        removing a node from the tree.'''
        pass

    def _find(self, key, node):
        '''searches the tree for the given key, returning the node object if
        found.'''
        if node and key > node.key:
            return self._find(key, node.right)
        elif node and key < node.key:
            return self._find(key, node.left)
        else:
            return node


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
