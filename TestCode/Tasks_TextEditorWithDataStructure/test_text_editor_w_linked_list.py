"""
author : Loi Chai Lam
date : 8 Sep 2017
title : Testing for Assignment2 Task 5

This is a testing code to test the List Data structure under
folder "Tasks/TextEditorWithDataStructure/text_editor_w_linked_list.py.py"

"""
import sys  # nopep8
import os  # nopep8

# append the path of the parent directory
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname((os.path.dirname(os.path.realpath(__file__))))), 'DataStructure'))  # nopep8

from linked_list import LinkedList
from node import Node

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname((os.path.dirname(os.path.realpath(__file__))))), 'Tasks/TextEditorWithDataStructure'))  # nopep8

from text_editor_w_linked_list import Editor

import unittest


class TestList(unittest.TestCase):
    """
    Run the testing in class LinkedList
    """

    def test_append(self):
        """
        Check the append(self, item)
        """
        list1 = LinkedList()
        list1.append(9)
        self.assertEqual(list1, [9])
        list1.append(-100)
        self.assertNotEqual(list1, [9, -10])
        self.assertEqual(list1.count, 2)

    def test_eq(self):
        """
        Check the __eq__(self, other)
        """
        list1 = LinkedList()
        list1.append(9)
        list1.append(10)
        self.assertTrue(list1 == [9, 10])
        self.assertFalse(list1 == [9])
        self.assertFalse(list1 == [9, 19])

    def test_len(self):
        """
        Check the __len__(self)
        """
        list1 = LinkedList()
        self.assertEqual(len(list1), 0)
        list1.append(9)
        self.assertEqual(len(list1), 1)

    def test_contain(self):
        """
        Check the __contains__(self, item)
        """
        list1 = LinkedList()
        list1.append(1)
        list1.append(3)
        list1.append(5)
        list1.append(7)
        self.assertFalse(9 in list1)
        self.assertTrue(3 in list1)

    def test_str(self):
        """
        Check the __str__(self)
        """
        list1 = LinkedList()
        list1.append(1)
        list1.append(3)
        self.assertEqual(str(list1), "1\n3")
        self.assertNotEqual(str(list1), "5\n3")

    def test_valid_index(self):
        """
        Check the valid_index(self, index)
        """
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        self.assertTrue(list1.valid_index(0))
        self.assertTrue(list1.valid_index(-1))
        self.assertFalse(list1.valid_index(-11))
        self.assertFalse(list1.valid_index(4))

    def test_getitem(self):
        """
        Check the __getitem__(self, index)
        """
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        self.assertRaises(IndexError, list1.__getitem__, 10)
        self.assertEqual(list1[0], 1)
        self.assertEqual(list1[-1], 2)

    def test_setitem(self):
        """
        Check the __setitem__(self, index, item)
        """
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        self.assertRaises(IndexError, list1.__setitem__, 5, 11)
        list1[0] = 5
        self.assertEqual(list1[0], 5)
        list1[-2] = 10
        self.assertEqual(list1[-2], 10)

    def test_insert(self):
        """
        Check the insert(self, index, item)
        """
        list1 = LinkedList()
        list1.append(1)
        list1.append(3)
        list1.append(5)
        self.assertRaises(IndexError, list1.insert, 5, 11)
        self.assertRaises(IndexError, list1.insert, -9, 11)
        list1.insert(0, 5)
        self.assertEqual(list1[0], 5)
        list1.insert(3, 6)
        self.assertEqual(list1[3], 6)
        self.assertEqual(len(list1), 5)
        list1.insert(-5, 9)
        self.assertEqual(list1[0], 9)
        self.assertEqual(list1.count, 6)

    def test_delete(self):
        """
        Check the delete(self, index)
        """
        list1 = LinkedList()
        list1.append(1)
        list1.append(3)
        list1.append(5)
        self.assertRaises(IndexError, list1.delete, 5)
        self.assertRaises(IndexError, list1.delete, -8)
        list1.delete(0)
        self.assertEqual(list1, [3, 5])
        list1.delete(0)
        self.assertEqual(list1, [5])
        list1.delete(0)
        self.assertEqual(list1, [])
        self.assertRaises(IndexError, list1.delete, 0)
        self.assertEqual(list1.count, 0)

    def test_remove(self):
        """
        Check the remove(self, item)
        """
        list1 = LinkedList()
        list1.append(1)
        list1.append(3)
        list1.append(1)
        list1.append(5)
        self.assertRaises(ValueError, list1.remove, 9)
        list1.remove(1)
        self.assertEqual(list1, [3, 1, 5])
        self.assertEqual(list1.count, 3)

    def test_sort(self):
        """
        Check the sort(self, reverse)
        """
        list1 = LinkedList()
        list1.sort(True)
        self.assertEqual(list1, [])
        list1.append(9)
        list1.append(3)
        list1.append(-10)
        list1.append(5)
        list1.sort(True)
        self.assertEqual(list1, [9, 5, 3, -10])
        list2 = LinkedList()
        list2.append(9)
        list2.append(3)
        list2.append(-10)
        list2.append(5)
        list2.sort(False)
        self.assertEqual(list2, [-10, 3, 5, 9])

    def test_get_node(self):
        """
        Check the _get_node(self, index)
        """
        list1 = LinkedList()
        list1.append(0)
        list1.append(1)
        list1.append(2)
        node = list1._get_node(0)
        self.assertEqual(node.item, 0)
        self.assertRaises(IndexError, list1._get_node, 3)
        self.assertRaises(IndexError, list1._get_node, -4)

    """
    Run the testing in class Editor
    """

    def test_read(self):
        """
        Check the read(self, filename)
        """
        editor = Editor()
        filename = "input.txt"
        editor.read(filename)
        self.assertEqual(editor.thelist[0], "I")
        self.assertEqual(len(editor.thelist), 11)

    def test_write(self):
        """
        Check the write(self, other)
        """
        editor = Editor()
        filename1 = "input.txt"
        filename2 = "aaa.txt"
        editor.read(filename1)
        editor.write(filename2)
        editor1 = Editor()
        editor1.read(filename2)
        self.assertEqual(editor1.thelist[0], "I")
        self.assertEqual(len(editor1.thelist), 11)

    def test_search(self):
        """
        Check the search(self, word)
        """
        editor = Editor()
        editor.insert(0, "a.")
        editor.insert(0, "b!!!")
        editor.insert(0, "c--")
        output = editor.search("b")
        self.assertEqual(1, output[0])
        output = editor.search("A")
        self.assertEqual(2, output[0])
        self.assertEqual(editor.search("f"), False)

    def test_print(self):
        """
        Check the print(self, num1, num2)
        """
        editor = Editor()
        editor.insert(0, "a")
        editor.insert(0, "b")
        editor.insert(0, "c")
        self.assertEqual(str(editor.thelist), "c\nb\na")
        editor.delete_index(0)
        self.assertEqual(str(editor.thelist), "b\na")

    def test_insert(self):
        """
        Check the insert(self, num, text)
        """
        editor = Editor()
        editor.insert(0, "a")
        editor.insert(0, "b")
        editor.insert(0, "c")
        self.assertRaises(Exception, editor.insert, 6, "d")
        self.assertEqual(editor.thelist[0], "c")
        self.assertEqual(editor.thelist[1], "b")

    def test_delete_index(self):
        """
        Check the delete_index(self, num)
        """
        editor = Editor()
        editor.insert(0, "a")
        editor.insert(0, "b")
        editor.insert(0, "c")
        editor.delete_index(0)
        self.assertEqual(str(editor.thelist), "b\na")
        self.assertRaises(Exception, editor.delete_index, "d")
        self.assertEqual(len(editor.thelist), 2)

    def test_delete_all(self):
        """
        Check the delete_all(self)
        """
        editor = Editor()
        editor.insert(0, "a")
        editor.insert(0, "b")
        editor.insert(0, "c")
        self.assertEqual(len(editor.thelist), 3)
        editor.delete_all()
        self.assertEqual(len(editor.thelist), 0)


if __name__ == "__main__":
    unittest.main()
