# -*- coding: utf-8 -*-


import unittest

from src import day17


class Day17TestSuite(unittest.TestCase):
    """Test Suite for Day17"""

    def test_combi(self):
        self.assertEquals(day17.combi([20, 15, 10, 5, 5], 25, 0), 4)

    def test_part1(self):
        self.assertEquals(day17.combi([43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34,
                                       17, 17, 44, 36, 31, 46, 9, 27, 38], 150, 0), 1638)


if __name__ == '__main__':
    unittest.main()
