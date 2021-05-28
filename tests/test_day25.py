# -*- coding: utf-8 -*-


import unittest

from parameterized import parameterized

from src import day25


class Day25TestSuite(unittest.TestCase):
    """Test Suite for Day25"""

    @parameterized.expand([
        (1, 1, 20151125),
        (3, 2, 8057251),
    ])
    def test_code(self, row, column, expected):
        self.assertEquals(day25.code(row, column), expected)

    def _test_part1(self):
        self.assertEquals(day25.code(3010, 3019), 8997277)


if __name__ == '__main__':
    unittest.main()
