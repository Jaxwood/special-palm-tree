# -*- coding: utf-8 -*-


import unittest

from parameterized import parameterized
from src import day11


class Day11TestSuite(unittest.TestCase):
    """Test Suite for Day11"""

    @parameterized.expand([
        ('hijklmmn', False),
        ('abbceffg', False),
        ('abccegjk', False),
        ('abcdffaa', True),
        ('ghjaabcc', True),
        ('aaabcefg', False),
    ])
    def test_is_valid(self, candidate, expected):
        self.assertEquals(day11.is_valid(candidate), expected)

    @parameterized.expand([
        ('abcdefgh', 'abcdffaa'),
        ('ghijklmn', 'ghjaabcc'),
    ])
    def test_roll_password(self, candidate, expected):
        self.assertEquals(day11.roll_password(candidate), expected)

    def test_part1(self):
        self.assertEquals(day11.roll_password('hepxcrrq'), 'hepxxyzz')

    def test_part2(self):
        self.assertEquals(day11.roll_password('hepxxyzz', True), 'heqaabcc')


if __name__ == '__main__':
    unittest.main()
