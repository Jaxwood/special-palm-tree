# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized

from src import day22


class Day22TestSuite(unittest.TestCase):
    """Test Suite for Day22"""

    def test_part1(self):
        self.assertEquals(day22.play(), 1824)

    def test_part2(self):
        self.assertEquals(day22.play(True), 1937)


if __name__ == '__main__':
    unittest.main()
