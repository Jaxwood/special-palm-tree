# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized
from src import day04


class Day04TestSuite(unittest.TestCase):
    """Test Suite for Day04"""

    @parameterized.expand([
        ('abcdef', 609043),
        ('pqrstuv', 1048970),
    ])
    def test_find_md5_hash(self, candidate, expected):
        self.assertEquals(day04.hash_of(candidate), expected)

    def test_part1(self):
        self.assertEquals(day04.hash_of('ckczppom'), 117946)


if __name__ == '__main__':
    unittest.main()
