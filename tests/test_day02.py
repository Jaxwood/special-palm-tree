# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized
from src import day02


class Day02TestSuite(unittest.TestCase):
    """Test Suite for Day02"""

    @parameterized.expand([
        ('2x3x4', 58),
        ('1x1x10', 43),
    ])
    def test_wrapping_papaer(self, candidate, expected):
        self.assertEquals(day02.wrapping_paper([candidate]), expected)

    def test_part1(self):
        f = open('data/day02.txt')
        self.assertEquals(day02.wrapping_paper(f.readlines()), 1588178)


if __name__ == '__main__':
    unittest.main()
