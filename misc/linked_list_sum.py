import sys
# You have two linked lists where each list represents some positive number.
# The ith node in the list represents the ith digit (0-9) of the number.
# Return a new linked list which represents the sum of the two linked lists.


class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)


class Node(object):
    def __init__(self, val, old_head=None):
        self.value = val
        self.next = old_head

    def __str__(self):
        return ('Node: Value {}'.format(self.value))


def sum_two(l1, l2):
    summed = LinkedList()

    l1_next = l1.head
    l1_arr = []
    l2_next = l2.head
    l2_arr = []

    while l1_next:
        l1_arr.append(l1_next.value)
        l1_next = l1_next.next

    while l2_next:
        l2_arr.append(l2_next.value)
        l2_next = l2_next.next

    pass_along = 0


    for one, two in zip(l1_arr, l2_arr):
        print('Entering Pass', pass_along)
        s = int(one) + int(two) + pass_along
        pass_along = 1 if s >= 10 else 0
        print(one, two, s, pass_along)
        set_val = s - pass_along*10
        print(set_val)
        summed.add(Node(set_val))

    return summed


def main():
    # Make two lists
    l1 = LinkedList()
    l1.add('1')
    l1.add('2')
    l1.add('3')
    l1.add('4')
    l2 = LinkedList()
    l2.add('0')
    l2.add('9')
    l2.add('9')
    l2.add('8')

    # Send to be summed
    summy = sum_two(l1, l2)
    summy_next = summy.head
    summy_arr = []

    while summy_next:
        print(summy_next.value)
        summy_arr.append(summy_next.value)
        summy_next = summy_next.next

    print(summy_arr)


main()
