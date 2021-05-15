# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized
from src import day05


class Day04TestSuite(unittest.TestCase):
    """Test Suite for Day05"""

    @parameterized.expand([
        ('ugknbfddgicrmopn', 1),
        ('aaa', 1),
        ('jchzalrnumimnmhp', 0),
        ('haegwjzuvuyypxyu', 0),
        ('dvszwmarrgswjxmb', 0),
    ])
    def test_find_nice_strings(self, candidate, expected):
        self.assertEquals(day05.find_nice_strings(
            [candidate]), expected)

    @parameterized.expand([
        ('qjhvhtzxzqqjkmpb', 1),
        ('xxyxx', 1),
        ('uurcxstgmygtbstg', 0),
        ('ieodomkazucvgmuy', 0),
    ])
    def test_find_even_nicer_strings(self, candidate, expected):
        self.assertEquals(day05.find_even_nicer_strings(
            [candidate]), expected)

    def test_part1(self):
        f = open('data/day05.txt')
        self.assertEquals(day05.find_nice_strings(
            f.readlines()), 255)

    def test_part2(self):
        f = open('data/day05.txt')
        self.assertEquals(day05.find_even_nicer_strings(
            f.readlines()), 55)


if __name__ == '__main__':
    unittest.main()
