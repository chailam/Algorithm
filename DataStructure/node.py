"""
author : Loi Chai Lam
date : 8 Sep 2017
title : Assignment2 Node

Node
Node used to create the node for linked list/linked stack.
It has attribute to save the value and the next item.
"""


class Node:
    """
    The class,Node used to create the node for linked list/linked stack

    """

    def __init__(self, item, link):
        """
        The initialise method in the Node
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : item : the item need to be inserted
                   link : whe the node link to
        return : -

        """
        self.item = item
        self.next = link
