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
    def test_wrapping_paper(self, candidate, expected):
        self.assertEquals(day02.wrapping_paper([candidate]), expected)

    @parameterized.expand([
        ('2x3x4', 34),
        ('1x1x10', 14),
    ])
    def test_bowtie(self, candidate, expected):
        self.assertEquals(day02.calculate_bowtie([candidate]), expected)

    def test_part1(self):
        f = open('data/day02.txt')
        self.assertEquals(day02.wrapping_paper(f.readlines()), 1588178)

    def test_part2(self):
        f = open('data/day02.txt')
        self.assertEquals(day02.calculate_bowtie(f.readlines()), 3783758)


if __name__ == '__main__':
    unittest.main()
