#!/usr/bin/env python3
import os
import sys

from tree import BTree


def main(arguments):
    btree = BTree()

    btree.set('c', 'C')
    btree.set('h', 'H')
    btree.set('a', 'A')
    btree.set('e', 'E')
    btree.set('f', 'F')
    btree.set('d', 'D')
    btree.set('b', 'B')
    btree.set('j', 'J')
    btree.set('g', 'G')
    btree.set('i', 'I')
    btree.set('k', 'K')

    print('Initial Tree:')
    btree.debug_print()

    print('Lookups:')
    print(btree.get('f'))
    print(btree.get('b'))
    print(btree.get('i'))

    print('')
    print('BFS:')
    btree.walk_bfs()

    print('')
    print('DFS preorder:')
    btree.walk_dfs_preorder(btree.root)

    print('')
    print('DFS inorder:')
    btree.walk_dfs_inorder(btree.root)

    print('')
    print('DFS postorder:')
    btree.walk_dfs_postorder(btree.root)

    print('')
    print('Remove b:')
    btree.remove('b')
    btree.debug_print()

    print('')
    print('Remove f:')
    btree.remove('f')
    btree.debug_print()

    print('')
    print('Remove h:')
    btree.remove('h')
    btree.debug_print()

if __name__ == '__main__':
    main(sys.argv)


# The `example_output.txt` file contains a printout of my code.  Please follow this format in creating your own `output.txt`.  It does not need to match my format exactly, but it should be close.  In particular, be sure to print the node key and parent key in the calls to `debug_print()`.
