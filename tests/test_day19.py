# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized

from src import day19


class Day19TestSuite(unittest.TestCase):
    """Test Suite for Day19"""

    @parameterized.expand([
        ('HOH', 4),
        ('HOHOHO', 7),
    ])
    def test_once(self, molecule, expected):
        replacements = [
            'H => HO',
            'H => OH',
            'O => HH',
        ]
        self.assertEquals(day19.replace_once(replacements, molecule), expected)

    @parameterized.expand([
        ('HOH', 3),
        ('HOHOHO', 6),
    ])
    def test_many(self, molecule, expected):
        replacements = [
            'e => H',
            'e => O',
            'H => HO',
            'H => OH',
            'O => HH',
        ]
        self.assertEquals(day19.find_replacements(
            replacements, molecule), expected)

    def test_part1(self):
        f = open('data/day19.txt')
        self.assertEquals(day19.replace_once(
            f.read().splitlines(), 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'), 509)

    def test_part2(self):
        f = open('data/day19.txt')
        self.assertEquals(day19.find_replacements(
            f.read().splitlines(), 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'), 195)


if __name__ == '__main__':
    unittest.main()
