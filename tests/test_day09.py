# -*- coding: utf-8 -*-


import unittest
from src import day09


class Day09TestSuite(unittest.TestCase):
    """Test Suite for Day09"""

    def test_shortest_distance(self):
        routes = ["London to Dublin = 464",
                  "London to Belfast = 518",
                  "Dublin to Belfast = 141"]
        self.assertEquals(day09.find_distance(
            routes, min), 605)

    def test_part1(self):
        f = open('data/day09.txt')
        self.assertEquals(day09.find_distance(
            f.readlines(), min), 117)

    def test_part2(self):
        f = open('data/day09.txt')
        self.assertEquals(day09.find_distance(
            f.readlines(), max), 909)


if __name__ == '__main__':
    unittest.main()
