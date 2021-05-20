# -*- coding: utf-8 -*-


import unittest

from src import day16


class Day16TestSuite(unittest.TestCase):
    """Test Suite for Day16"""

    def test_part1(self):
        aunts = [
            ('children', 3),
            ('cats', 7),
            ('samoyeds', 2),
            ('pomeranians', 3),
            ('akitas', 0),
            ('vizslas', 0),
            ('goldfish', 5),
            ('trees', 3),
            ('cars', 2),
            ('perfumes', 1),
        ]
        f = open('data/day16.txt')
        self.assertEquals(day16.find_aunt_sue(aunts, f.readlines()), 40)


if __name__ == '__main__':
    unittest.main()
