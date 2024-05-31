"""
author : Loi Chai Lam
date   : 7 Sep 2017

Sorted Linked List

Note that this is a PARTIAL sorted linked list as it only has "add" and "print" function.

A linked list consists of a data element known as a node. 
And each node consists of two fields: one field has data, 
and in the second field, the node has an address that keeps a reference to the next node.

The sorted linked list the the linked list that is sorted.

"""

from node import Node


class SortedLinkedList:
    """
    the class sorted linked list
    """

    def __init__(self):
        self.head = None

    def add(self, item):
        """
        add item in sorted linked list in ascending order
        """
        # if empty
        if self.head == None:
            self.head = Node(item, None)
        # if smallest
        elif self.head.item >= item:
            self.head = Node(item, self.head)
        # find a position to add before,
        # or add as last(when current become None)
        else:
            previous = self.head
            current = previous.next
            while current is not None:
                if current.item >= item:
                    break
                previous = current
                current = current.next
            previous.next = Node(item, current)


    def __str__(self):
        """
        print the item in sirted linked list
        """
        string = ""
        current = self.head
        while current is not None:
            string += str(current) + ","  # 因为Node有str了,所以可以直接str(current)
            current = current.next
        return string
