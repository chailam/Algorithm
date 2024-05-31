"""
author : Loi Chai Lam
date   : 7 Sep 2017

Binary Search Tree

A data structure used in computer science for organizing and storing data in a sorted manner. 
Each node in a Binary Search Tree has at most two children, a left child and a right child, 
with the left child containing values less than the parent node and the right child containing 
values greater than the parent node. This hierarchical structure allows for efficient searching, 
insertion, and deletion operations on the data stored in the tree.

"""
from sorted_linked_list import SortedLinkedList


class TreeNode:
    """
    the node of the class BinarySearchTree
    """

    def __init__(self, key, item, left=None, right=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.item)


class BinarySearchTree:
    """
    the class BinarySearchTree
    """

    def __init__(self):
        self.root = None

    def __setitem__(self, key, item):
        """
        adding the item to the tree
        """
        # if self.root == None:
        #    self.root = Node(item, None)
        self.root = self.setitem_aux(self.root, key, item)

    def setitem_aux(current, key, item):
        """
        auxiliary function of the setitem
        """
        if current is None:
            linkedList = SortedLinkedList
            linkedList.add(item)
            current.item = linkedList
        elif key < current.key:
            current.left = self.setitem_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.setitem_aux(current.right, key, item)
        else:
            linkedList = current.item
            linkedList.add(item)
            current.item = linkedList
        return current

    def __getitem__(self, key):
        """
        searching the item in the tree
        """
        return self.getitem_aux(self.root, key)


    def getitem_aux(self, current, key):
        """
        auxiliary function of the getitem
        """
        if current is None:
            raise KeyError("key not found")
        elif key < current.key:
            return self.getitem_aux(current.left, key)
        elif key > current.key:
            return self.getitem_aux(current.right, key)
        else:
            return current.item

    def __str__(self, order="inorder"):
        return self.print_inorder()

    def print_inorder(self):
        """
        transverse the tree in inoder
        """
        self.print_inorder_aux(self.root)

    def print_inorder_aux(self, current):
        """
        auxiliary function of the print_inorder
        """
        if current is not None:
            self.print_inorder_aux(current.left)
            print(current.item)
            self.print_inorder_aux(current.right)
