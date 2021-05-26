# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized

from src import day22


class Day22TestSuite(unittest.TestCase):
    """Test Suite for Day22"""

    def test_part1(self):
        self.assertEquals(day22.part1(), 1824)


if __name__ == '__main__':
    unittest.main()
