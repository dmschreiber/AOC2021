import unittest
import day2

class MyTestCase(unittest.TestCase):
    def test_day1(self):
        self.assertEqual(day2.part1("./data/day2_test.txt"),"150")
        self.assertEqual(day2.part2("./data/day2_test.txt"),"900")


if __name__ == '__main__':
    unittest.main()
