# -*- coding: utf-8 -*-


import unittest

from src import day18


class Day18TestSuite(unittest.TestCase):
    """Test Suite for Day18"""

    def test_light_switcher(self):
        grid = [
            '.#.#.#',
            '...##.',
            '#....#',
            '..#...',
            '#.#..#',
            '####..',
        ]
        self.assertEquals(day18.light_switcher(grid, 4), 4)

    def test_part1(self):
        f = open('data/day18.txt')
        self.assertEquals(day18.light_switcher(
            f.read().splitlines(), 100), 821)


if __name__ == '__main__':
    unittest.main()
