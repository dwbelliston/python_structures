# Assignment: Binary Tree

Write a binary tree class that has the following methods:

1. `set(key, value)` stores a key=value pair to the tree in the appropriate spot.
1. `get(key)` returns the value stored with the given key.  If the key does not exist, null/None should be returned.
1. `remove(key)` removes the node with the given key from the tree.  If the key does not exist, it should simply return (no error).
1. `walk_dfs_inorder()` iterates through the nodes of the tree in depth-first-search "inorder" order.
1. `walk_dfs_preorder()` iterates through the nodes of the tree in depth-first-search "preorder" order.
1. `walk_dfs_postorder()` iterates through the nodes of the tree in depth-first-search "postorder" order.
1. `walk_bfs()` iterates through the nodes of the tree in breadth-first-search order.
1. `debug_print()` prints a graphical representation of the tree. See below for more information.

You can adjust the API of above methods if needed, but be sure to implement the behavior specified.

The tree has at least one field, `root`, that is the top node of the tree.


## Node

Each node of the binary tree should be an instance of your `Node` class.  Create this class with the following fields:

1. `key` - the key the item is stored under.  The placement of the node in the tree is based on this key.
1. `value` - the value being stored (string or object is fine).
1. `parent` - a reference to the parent of the node.
1. `left` - a reference to the left child of the node.
1. `right` - a reference to the right child of the node.

When the tree is modified (`set`, `remove`), be sure to update the `parent`, `left`, and `right` references.

I suggest you also create a `toString()` or `__str__()` or `description` property to make printing nodes easy.  My method prints the node key and parent with parentheses: `key(parentkey)`.


## Removing a Node

Arguably, the most difficult part of this assignment is removal of a key/value from the tree.  Since your node objects define the structure (references) of the tree, removal of a node creates a hole in the reference graph.  These way you handle a removal depends on the type of hole that is created:

* If the node has no children, it is a leaf node in the tree.  Just remove the node.
* If the node has one child, replace it with the child node.
* If the node has two children, things get a little more difficult.  You need to replace it with the next-closest node (closest by *key*).  Finding the next closest node can be done by 1) walking its left child tree and finding the largest key value, or 2) walking its right child tree and finding the smallest key value.  In either case, the replacement node will be a leaf node.  Move the leave node in place of the one that you are removing.


## Helper Methods

YMMV, but if it helps, I added two additional, private methods to my tree class for use by the public methods:

1. `_replace_node(oldnode, newnode)` - replaces a node with another node in the tree.  This is useful when removing a node from the tree.
1. `_find(key)` - searches the tree for the given key, returning the node object if found.

I programmed the various `walk_...` methods as generators.  Another is to create an iterator object in your language's way and return that iterator.  If nothing else, create a list during the walk and return the list (this method uses more memory).


## Main Method

In your main code loop, perform the following operations:

1. Create the tree by storing following key=value pairs:
        c = C
        h = H
        a = A
        e = E
        f = F
        d = D
        b = B
        j = J
        g = G
        i = I
        k = K
1. Print the tree with `debug_print()`.
1. Print the value with key = `f`.
1. Print the value with key = `b`.
1. Print the value with key = `i`.
1. Walk the tree in `BFS` order and print each value.
1. Walk the tree in `DFS preorder` order and print each value.
1. Walk the tree in `DFS inorder` order and print each value.
1. Walk the tree in `DFS postorder` and print each value.
1. Remove the value with key = `b`.
1. Print the tree with `debug_print()`.
1. Remove the value with key = `f`.
1. Print the tree with `debug_print()`.
1. Remove the value with key = `h`.
1. Print the tree with `debug_print()`.

The initial tree will look as follows:

         c
    a              h
      b       e          j
            d   f      i   k
                  g

The `example_output.txt` file contains a printout of my code.  Please follow this format in creating your own `output.txt`.  It does not need to match my format exactly, but it should be close.  In particular, be sure to print the node key and parent key in the calls to `debug_print()`.

## Submitting the Assignment

Zip your code files and output.txt submit on Learning Suite.