# -*- coding: utf-8 -*-


import unittest

from src import day14


class Day14TestSuite(unittest.TestCase):
    """Test Suite for Day14"""

    def test_travel(self):
        travel_distances = [
            'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
            'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
        ]
        self.assertEquals(day14.travel(travel_distances, 1000), 1120)

    def test_part1(self):
        f = open('data/day14.txt')
        self.assertEquals(day14.travel(f.readlines(), 2503), 2655)

    def test_part2(self):
        f = open('data/day14.txt')
        self.assertEquals(day14.travel(f.readlines(), 2503, True), 1059)


if __name__ == '__main__':
    unittest.main()
