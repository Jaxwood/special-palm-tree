# -*- coding: utf-8 -*-


import unittest
from src import day09


class Day09TestSuite(unittest.TestCase):
    """Test Suite for Day09"""

    def test_shortest_distance(self):
        routes = ["London to Dublin = 464",
                  "London to Belfast = 518",
                  "Dublin to Belfast = 141"]
        self.assertEquals(day09.find_shortest_distance(
            routes), 605)

    def test_part1(self):
        f = open('data/day09.txt')
        self.assertEquals(day09.find_shortest_distance(
            f.readlines()), 117)


if __name__ == '__main__':
    unittest.main()
