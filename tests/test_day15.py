# -*- coding: utf-8 -*-


import unittest

from src import day15


class Day15TestSuite(unittest.TestCase):
    """Test Suite for Day15"""

    def test_mix2(self):
        reciepes = [
            'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
            'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
        ]
        self.assertEquals(day15.mix2(reciepes, 100), 62842880)

    def test_mix2_with_calories(self):
        reciepes = [
            'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
            'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
        ]
        self.assertEquals(day15.mix2(reciepes, 100, True), 57600000)

    def test_part1(self):
        f = open('data/day15.txt')
        self.assertEquals(day15.mix4(f.readlines(), 100), 13882464)

    def test_part2(self):
        f = open('data/day15.txt')
        self.assertEquals(day15.mix4(f.readlines(), 100, True), 11171160)


if __name__ == '__main__':
    unittest.main()
