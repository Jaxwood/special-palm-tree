# -*- coding: utf-8 -*-


import unittest

from parameterized import parameterized
from src import day13


class Day13TestSuite(unittest.TestCase):
    """Test Suite for Day13"""

    def test_seating(self):
        arrangement = [
            "Alice would gain 54 happiness units by sitting next to Bob.",
            "Alice would lose 79 happiness units by sitting next to Carol.",
            "Alice would lose 2 happiness units by sitting next to David.",
            "Bob would gain 83 happiness units by sitting next to Alice.",
            "Bob would lose 7 happiness units by sitting next to Carol.",
            "Bob would lose 63 happiness units by sitting next to David.",
            "Carol would lose 62 happiness units by sitting next to Alice.",
            "Carol would gain 60 happiness units by sitting next to Bob.",
            "Carol would gain 55 happiness units by sitting next to David.",
            "David would gain 46 happiness units by sitting next to Alice.",
            "David would lose 7 happiness units by sitting next to Bob.",
            "David would gain 41 happiness units by sitting next to Carol.",
        ]
        self.assertEquals(day13.seating(arrangement), 330)

    def test_part1(self):
        f = open('data/day13.txt')
        self.assertEquals(day13.seating(f.readlines()), 709)


if __name__ == '__main__':
    unittest.main()
