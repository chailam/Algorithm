"""
author : Loi Chai Lam
date : 27 Sep 2017
title : Testing for Assignment3 Task 1

This is a testing code to test the List Data structure under
folder "Data Structure/hash_table_linear_probing.py"

"""
import sys  # nopep8
import os  # nopep8

# append the path of the parent directory
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname((os.path.dirname(os.path.realpath(__file__))))), 'DataStructure'))  # nopep8

from hash_table_linear_probing import HashTableLinear

import unittest




class TestHashTableLinear(unittest.TestCase):
    """
    Run the testing in class HashTableLinear
    """

    def test_setitem(self):
        """
        Check the __setitem__(self, key, value)
        """
        table = HashTableLinear()
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertEqual(len(table), 3)
        self.assertEqual(table["FIT2100"], "OS")
        table["FIT2100"] = "HD"
        self.assertEqual(table["FIT2100"], "HD")
        for i in range(7916):
            table[str(i)] = i
        self.assertRaises(Exception, table.__setitem__, "HDhd", "HDhd")
        self.assertEqual(len(table), 7919)

    def test_getitem(self):
        """
        Check the __getitem__(self, key)
        """
        table = HashTableLinear()
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
        table = HashTableLinear()
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertEqual(len(table), 3)

    def test_str(self):
        """
        Check the __str__(self)
        """
        table = HashTableLinear()
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertEqual(str(table), "(FIT1008, Intro To Comp Sci)(FIT2100, OS)(FIT2101, Soft Eng Process Management)")

    def test_hashvalue(self):
        """
        Check the hash_value(self, key)
        """
        table = HashTableLinear()
        ans1 = table.hash_value("FIT1008")
        h = 0
        for c in "FIT1008":
            h = (h * 101 + ord(c)) % 7919
        self.assertEqual(ans1, h)

    def test_contain(self):
        """
        Check the __contains__(self, key)
        """
        table = HashTableLinear()
        table["FIT1008"] = "Intro To Comp Sci"
        table["FIT2101"] = "Soft Eng Process Management"
        table["FIT2100"] = "OS"
        self.assertTrue("FIT1008" in table)
        self.assertTrue("FIT2100" in table)
        self.assertFalse("FIT" in table)



if __name__ == "__main__":
    unittest.main()
