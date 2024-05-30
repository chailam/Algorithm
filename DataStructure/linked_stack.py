"""
author : Loi Chai Lam
date : 16 Sep 2017
title : Assignment2 Task 6_a (Linked Stack)

Linked Stack
This is the stack implemented using Node, instead of array, so that it behave like linked list 
but with stack feature
"""
from node import Node


class LinkedStack():
    """
    The class, LinkedStack is implemented using Node 
    """

    def __init__(self):
        """
        The initialise method in the stack
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : -
        return : -

        """
        self.top = None
        self.count = 0

    def push(self, item):
        """
        Push item to the Stack
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : item : the item need to be pushed to the stack
        return : -

        """
        self.top = Node(item, self.top)
        self.count += 1

    def pop(self):
        """
        Pop the item from the Stack
        precondition : -
        postcondition : -
        complexity: best : O(1) 
                    worst : O(1)
        argument : -
        return : item : the item poped from the Stack

        """
        assert self.count > 0, "Stack is empty"
        item = self.top.item
        self.top = self.top.next
        self.count -= 1
        return item

    def __str__(self):
        """
        The builtin method, called by str(self)
        precondition : -
        postcondition : -
        complexity: best : O(N) ,N is the length of the list  
                    worst : O(N),N is the length of the list 
        argument : -
        return : string representation of the list, which one item per line

        """
        string = ""
        current = self.top
        while not (current is None):
            string += str(current.item) + "\n"
            current = current.next
        return string




if __name__ == "__main__":
    stack = LinkedStack()
    stack.push([1, "read"])
    stack.push([2, "rd"])
    a = stack.pop()
    print(a[0])
    print(a[1])
