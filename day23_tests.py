import unittest
import time

import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23


class MyTestCase(unittest.TestCase):
    def test_day23(self):
        self.assertEqual(day23.part1("./data/day23_test.txt"),"12521")
        self.assertEqual(day23.part2("./data/day23_test.txt"),"44169")


if __name__ == '__main__':
    unittest.main()
