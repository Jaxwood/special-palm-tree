# -*- coding: utf-8 -*-


import unittest
from src import day07


class Day07TestSuite(unittest.TestCase):
    """Test Suite for Day07"""

    def test_wire_circuits(self):
        instructions = ["123 -> x",
                        "456 -> y",
                        "x AND y -> d",
                        "x OR y -> e",
                        "x LSHIFT 2 -> f",
                        "y RSHIFT 2 -> g",
                        "NOT x -> h",
                        "NOT y -> i"]
        self.assertEquals(day07.circuit(
            instructions)['i'], 65079)

    def test_part1(self):
        f = open('data/day07.txt')
        self.assertEquals(day07.circuit(
            f.readlines())['a'], 3176)


if __name__ == '__main__':
    unittest.main()
