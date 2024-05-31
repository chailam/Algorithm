"""
author : Loi Chai Lam
date : 28 Sep 2017
title : Testing for Assignment3 Task 5

This is a testing code to test the List Data structure under
folder "Data Structure/hash_table_separate_chaining.py"

"""
import sys  # nopep8
import os  # nopep8

# append the path of the parent directory
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname((os.path.dirname(os.path.realpath(__file__))))), 'DataStructure'))  # nopep8

from hash_table_separate_chaining import HashTableSeparateChaining
from node import Node
from linked_list import LinkedList

import unittest


class TestHashTableSeparateChaining(unittest.TestCase):
    """
    Run the testing in class HashTableSeparateChaining
    """

    def test_setitem(self):
        """
        Check the __setitem__(self, key, value)
        """
        table = HashTableSeparateChaining(101, 7919)
        table.__setitem__("FIT1008", "Intro To Comp Sci")
        table.__setitem__("FIT2101", "Soft Eng Process Management")
        result = table.__setitem__("FIT2100", "OS")
        self.assertEqual(len(table), 3)
        self.assertEqual(table["FIT2100"], "OS")


    def test_getitem(self):
        """
        Check the __getitem__(self, key)
        """
        table = HashTableSeparateChaining()
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertEqual(len(table), 3)
        self.assertEqual(table["FIT2100"], "OS")
        self.assertRaises(KeyError, table.__getitem__, "HDhd")
        self.assertEqual(len(table), 3)

    def test_len(self):
        """
        Check the __len__(self)
        """
        table = HashTableSeparateChaining()
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertEqual(len(table), 3)

    def test_str(self):
        """
        Check the __str__(self)
        """
        table = HashTableSeparateChaining(101, 3)
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertEqual(str(table), "(FIT2101, Soft Eng Process Management)(FIT1008, Intro To Comp Sci)(FIT2100, OS)")

    def test_hashvalue(self):
        """
        Check the hash_value(self, key)
        """
        table = HashTableSeparateChaining(151, 399989)
        ans1 = table.hash_value("FIT1008")
        h = 0
        table_size = 399989
        for c in "FIT1008":
            h = (h * 151 + ord(c)) % table_size
        self.assertEqual(ans1, h)

    def test_contain(self):
        """
        Check the __contains__(self, key)
        """
        table = HashTableSeparateChaining()
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertTrue("FIT1008" in table)
        self.assertTrue("FIT2100" in table)
        self.assertFalse("FIT" in table)

    def test_read(self):
        """
        Check the read(filename, size)
        """
        filename = "aaa.txt"
        size = 399989
        a = 101
        value = read(filename, a, size)
        self.assertEqual(value[1], 0)
        self.assertEqual(value[2], 0)

    """
    Run the testing in class LinkedList
    """

    def test_append(self):
        """
        Check the append(self, item)
        """
        list1 = LinkedList()
        list1.append(9)
        self.assertEqual(str(list1), "9")
        list1.append(-100)
        self.assertNotEqual(str(list1), [9, -10])
        self.assertEqual(list1.count, 2)

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




if __name__ == "__main__":
    unittest.main()
