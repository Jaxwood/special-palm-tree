# -*- coding: utf-8 -*-


import unittest

from parameterized import parameterized
from src import day10


class Day10TestSuite(unittest.TestCase):
    """Test Suite for Day10"""

    @parameterized.expand([
        ('1', '11'),
        ('11', '21'),
        ('21', '1211'),
        ('1211', '111221'),
        ('111221', '312211'),
    ])
    def test_look_and_say(self, candidate, expected):
        self.assertEquals(day10.look_and_say(candidate, 1), expected)

    def test_part1(self):
        self.assertEquals(len(day10.look_and_say('3113322113', 40)), 329356)


if __name__ == '__main__':
    unittest.main()
