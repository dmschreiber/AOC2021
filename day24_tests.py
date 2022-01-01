import unittest
import time

import day24


class MyTestCase(unittest.TestCase):
    def test_day24(self):
        # self.assertEqual(day24.part1("./data/day24_test.txt","39"),"1")
        # self.assertEqual(day24.part1("./data/day24_test2.txt","123"),"6")
        # self.assertEqual(day24.part1("./data/day24_test3.txt","7"),"1")
        # self.assertEqual(day24.part1("./data/day24_test3.txt","2"),"0")
        self.assertEqual(day24.part1("./data/day24.txt"),"0")

if __name__ == '__main__':
    unittest.main()
