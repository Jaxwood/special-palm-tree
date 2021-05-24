# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized

from src import day21
from src.day21 import Player


class Day21TestSuite(unittest.TestCase):
    """Test Suite for Day21"""

    def test_part1(self):
        self.assertEquals(day21.fight(), 111)


if __name__ == '__main__':
    unittest.main()
