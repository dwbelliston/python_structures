#!/usr/bin/env python3
from queue import Queue

ll = Queue()
ll.enqueue('a')
ll.enqueue('b')
ll.enqueue('c')
ll.debug_print()
print(ll.dequeue())
ll.enqueue('d')
ll.debug_print()
print(ll.dequeue())
print(ll.dequeue())
ll.debug_print()
print(ll.size)
