"""
author : Loi Chai Lam
date : 27 Sep 2017
title : Testing for Assignment3 Task 4

This is a testing code to test the List Data structure under
folder "Data Structure/hash_table_quadratic_probing.py"

"""
import sys  # nopep8
import os  # nopep8

# append the path of the parent directory
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname((os.path.dirname(os.path.realpath(__file__))))), 'DataStructure'))  # nopep8

from hash_table_quadratic_probing import HashTableQuadratic

import unittest


class TestHashTableQuadratic(unittest.TestCase):
    """
    Run the testing in class HashTableQuadratic
    """

    def test_setitem(self):
        """
        Check the __setitem__(self, key, value)
        """
        table = HashTableQuadratic(101, 7919)
        table.__setitem__("FIT1008", "Intro To Comp Sci")
        table.__setitem__("FIT2101", "Soft Eng Process Management")
        result = table.__setitem__("FIT2100", "OS")
        self.assertEqual(len(table), 3)


    def test_getitem(self):
        """
        Check the __getitem__(self, key)
        """
        table = HashTableQuadratic()
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
        table = HashTableQuadratic()
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertEqual(len(table), 3)

    def test_str(self):
        """
        Check the __str__(self)
        """
        table = HashTableQuadratic()
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertEqual(str(table), "(FIT2100, OS)(FIT2101, Soft Eng Process Management)(FIT1008, Intro To Comp Sci)")

    def test_hashvalue(self):
        """
        Check the hash_value(self, key)
        """
        table = HashTableQuadratic(151, 399989)
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
        table = HashTableQuadratic()
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

    def test_modify_size(self):
        """
        Check the modify_size(self)
        """
        size = 5
        a = 151
        table = HashTableQuadratic(a, size)
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        self.assertEqual(table.table_size, 5)
        table["FIT2100"] = "OS"
        table["FIT2004"] = "Hardest"
        table["FIT1045"] = "Python"
        self.assertEqual(table.table_size, 11)






if __name__ == "__main__":
    unittest.main()
