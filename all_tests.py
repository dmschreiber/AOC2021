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

class MyTestCase(unittest.TestCase):
    def test_day1(self):
        self.assertEqual(day2.part1("./data/day2_test.txt"),"150")
        self.assertEqual(day2.part2("./data/day2_test.txt"),"900")

    def test_day3(self):
        self.assertEqual(day3.part1("./data/day3_test.txt"),"198")
        self.assertEqual(day3.part2("./data/day3_test.txt"),"230")

    def test_day4(self):
        self.assertEqual(day4.part1("./data/day4_test.txt"),"4512")
        self.assertEqual(day4.part2("./data/day4_test.txt"),"1924")
    def test_day5(self):
        self.assertEqual(day5.part1("./data/day5_test.txt"),"5")
        self.assertEqual(day5.part2("./data/day5_test.txt"),"12")

    def test_day6(self):
        self.assertEqual(day6.part1("./data/day6_test.txt",80),"5934")
        self.assertEqual(day6.part2("./data/day6_test.txt",256),"26984457539")

    def test_day7(self):
        self.assertEqual(day7.part1("./data/day7_test.txt"),"37")
        self.assertEqual(day7.part2("./data/day7_test.txt"),"168")

    def test_day8(self):
        self.assertEqual(day8.part1("./data/day8_test.txt"),"26")
        self.assertEqual(day8.part2("./data/day8_test.txt"),"61229")

    def test_day9(self):
        self.assertEqual(day9.part1("./data/day9_test.txt"),"15")
        self.assertEqual(day9.part2("./data/day9_test.txt"),"1134")

    def test_day10(self):
        self.assertEqual(day10.part1("./data/day10_test.txt"),"26397")
        self.assertEqual(day10.part2("./data/day10_test.txt"),"288957")

    def test_day11(self):
        map = day11.read_map("./data/day11_test.txt")
        after_step1 =day11.read_map("./data/day11_test_afterstep2.txt")

        print("{}\n{}".format(map, after_step1))
        count = 0
#        print("Step 1")
        (map,count) = day11.step(map,count)
#        day11.print_map(map)
#        print("Step 2")
        (map,count) = day11.step(map,count)
#        day11.print_map(map)
        self.assertEqual(map,after_step1)
        self.assertEqual(day11.part1("./data/day11_test.txt"),"1656")
        self.assertEqual(day11.part2("./data/day11_test.txt"),"195")

    def test_day12(self):
        self.assertEqual(day12.is_small("start"),True)
        self.assertEqual(day12.is_small("hw"),True)
        self.assertEqual(day12.is_small("WI"),False)

        self.assertEqual(day12.path_has_two_small_caves(["start","W","a","a"]),True)
        self.assertEqual(day12.path_has_two_small_caves(["start","W","b","a"]),False)
        self.assertEqual(day12.path_has_two_small_caves(["start", "W","a","W","a"]),True)

        self.assertEqual(day12.part1("./data/day12_test.txt"),"226")
        start_time = time.perf_counter()
        self.assertEqual(day12.part2("./data/day12_test.txt"),"3509")
        end_time = time.perf_counter()
        print(f"Day 12 part 2 execution Time : {end_time - start_time:0.6f}")

    def test_day13(self):
        self.assertEqual(day13.part1("./data/day13_test.txt"),"17")
        self.assertEqual(day13.part2("./data/day13_test.txt"),"")

    def test_day14(self):
        self.assertEqual(day14.score_polymer("NNCB"),1)
        self.assertEqual(day14.part1("./data/day14_test.txt"),"1588")
        self.assertEqual(day14.part2("./data/day14_test.txt"),"2188189693529")

    def test_day15(self):
        self.assertEqual(day15.part1("./data/day15_test.txt"),"40")
        self.assertEqual(day15.part2("./data/day15_test.txt"),"315")

if __name__ == '__main__':
    unittest.main()
