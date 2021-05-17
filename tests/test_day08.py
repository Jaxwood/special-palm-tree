# -*- coding: utf-8 -*-


import unittest
from src import day08


class Day08TestSuite(unittest.TestCase):
    """Test Suite for Day08"""

    def test_storage_amount(self):
        string_literal = [r'""',
                          r'"abc"',
                          r'"aaa\"aaa"',
                          r'"\x27"']
        self.assertEquals(day08.storage_amount(
            string_literal), 12)

    def test_storage_escaped_amount(self):
        string_literal = [r'""',
                          r'"abc"',
                          r'"aaa\"aaa"',
                          r'"\x27"']
        self.assertEquals(day08.storage_escaped_amount(
            string_literal), 19)

    def test_part1(self):
        f = open('data/day08.txt')
        self.assertEquals(day08.storage_amount(
            f.read().splitlines()), 1350)

    def test_part2(self):
        f = open('data/day08.txt')
        self.assertEquals(day08.storage_escaped_amount(
            f.read().splitlines()), 2085)


if __name__ == '__main__':
    unittest.main()
