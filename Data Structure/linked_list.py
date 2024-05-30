"""
author : Loi Chai Lam
date : 8/9/2017
title : Assignment2 Task 5_a (Linked List)

Linked List
A linked list consists of a data element known as a node. 
And each node consists of two fields: one field has data, 
and in the second field, the node has an address that keeps a reference to the next node.
"""


class Node:
    """
    The class,Node used to create the node for linked list

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


class LinkedList:
    """
    The class, LinkedList is implemented using Node

    """

    def __init__(self):
        """
        The initialise method in the list
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : -
        return : -

        """
        self.head = None
        self.count = 0

    def __len__(self):
        """
        The builtin method, called by len(self)
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : -
        return : the length of the list, which is self.count

        """
        return self.count

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
        for i in range(len(self) - 1):
            string += str(self[i]) + "\n"
        if len(self) > 0:
            string += str(self[len(self) - 1])
        return string

    def __contains__(self, item):
        """
        The builtin method in the list, called by item in self
        precondition : -
        postcondition : -
        complexity: best : O(1), if list[0] is the item which need to find 
                    worst : O(N) ,N is the length of the list , if item not in the list
        argument : item : the item which need to check
        return : True if item is in the list, False otherwise

        """
        for i in range(len(self)):
            if item == self[i]:
                return True
        return False

    def valid_index(self, index):
        """
        To check the validity of the index
        precondition : -
        postcondition : -
        complexity: best : O(1) 
                    worst : O(1)
        argument : index : the index need to be checked
        return : True if is valid index, False otherwise

        """
        return index < len(self) and index >= -len(self)

    def _get_node(self, index):
        """
        To get the node of certain index
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(N), where N is the index
                    worst : O(N), where N is the index
        argument : index : the index of the node need to get
        return : the required node

        """
        if not self.valid_index(index):
            raise IndexError("Invalid Index")
        if index < 0:
            index = len(self) + index
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def __getitem__(self, index):
        """
        The builtin method in the list, called by self[index], it returns the index in the list
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(N), where N is the index
                    worst : O(N), where N is the index
        argument : index : the required index in the list
        return : returns the item at index in the list, if index is non-negative.
                 If it is negative, it will return the last item if index is −1, the second-to last if index is −2,
                 and so on up to minus the length of the list, which returns the first item

        """
        if not self.valid_index(index):
            raise IndexError("Invalid Index")
        if index < 0:
            index = len(self) + index
        node = self._get_node(index)
        return node.item

    def __setitem__(self, index, item):
        """
        The builtin method in the list, called by self[index] = item, sets the value at index in the list to be item
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(N), where N is the index
                    worst : O(N), where N is the index
        argument : index : the required index in the list
                   item : the required item which need to set
        return : -

        """
        if not (index <= len(self) and index >= -len(self)):
            raise IndexError("Invalid Index")
        if index < 0:
            index = len(self) + index
        node = self._get_node(index)
        node.item = item

    def __eq__(self, other):
        """
        The builtin method in the list, called by self == other
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(1) ,if the length of the array not equal to the other or if the self.array[0] != other[0]
                    worst : O(N) ,N is the length of the list , if all items are same
        argument : other : other list to be compared
        return : True if this list is equivalent to other

        """
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def append(self, item):
        """
        Adds item to the end of the list
        precondition : -
        postcondition : -
        complexity: best :  O(N), where N is the length of the list 
                    worst : O(N), where N is the length of the list
        argument : item : the item need to be added
        return : -

        """
        if self.head == None:
            self.head = Node(item, None)
        else:
            node = self._get_node(len(self) - 1)
            node.next = Node(item, None)
        self.count += 1

    def insert(self, index, item):
        """
        Inserts item into self before position index
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(N) ,N is index
                    worst : O(N) ,N is index
        argument : item : the item need to be inserted
                   index : the index of the item need to be inserted
        return : -

        """
        if not (index <= len(self) and index >= -len(self)):
            raise IndexError("Invalid Index")
        if index < 0:
            index = len(self) + index
        if index == 0:
            self.head = Node(item, self.head)
        else:
            node = self._get_node(index - 1)
            node.next = Node(item, node.next)
        self.count += 1

    def delete(self, index):
        """
        Deletes the item at index from the list,
        moving all items after it towards the start of the list
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(N), N is index
                    worst : O(N), N is index
        argument : index : the index of the item need to be deleted
        return : -

        """
        if not self.valid_index(index):
            raise IndexError("Invalid Index")
        if index < 0:
            index = len(self) + index
        if index == 0:
            self.head = self.head.next
        else:
            node = self._get_node(index - 1)
            node.next = node.next.next
        self.count -= 1

    def remove(self, item):
        """
        Delete the first instance of item from the list
        precondition : the item must exist in the list
        postcondition : -
        complexity: best : O(1) ,if the target item is first item in the list
                    worst : O(N), N is the length of the list, if the index of the item is the last index 
        argument : item : the item in the first instance need to be deleted
        return : -

        """
        if not (item in self):
            raise ValueError("Item does not exist")
        for i in range(len(self)):
            if item == self[i]:
                self.delete(i)
                break

    def sort(self, reverse):
        """
        Sorts the items in the list using bubble sort
        precondition : -
        postcondition : -
        complexity: best : O(N) ,N is the length of the list, if the list is sorted
                    worst : O(N**2), N is the length of the list, if the list is not sorted and it needs to loop twice
        argument : reverse : if reverse is False, sort the list in ascending order
                             if reverse is True, sort the list in descending order
        return : -

        """
        for i in range(len(self) - 1):
            swapped = False
            for j in range(len(self) - 1 - i):
                if reverse == False:
                    if self[j] > self[j + 1]:
                        self[j], self[j + 1] = self[j + 1], self[j]
                        swapped = True
                elif reverse == True:
                    if self[j] < self[j + 1]:
                        self[j], self[j + 1] = self[j + 1], self[j]
                        swapped = True
            if not swapped:
                break


if __name__ == "__main__":
    list1 = LinkedList()
    list1.insert(0, 0)
    list1.insert(1, 1)
    list1.insert(2, 2)
    list1.append(3)
    list1.append(-100)
    list1.append(5)
    list1.append(7)
    list1.sort(False)
    print(list1)
