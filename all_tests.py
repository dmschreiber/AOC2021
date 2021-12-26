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

    def test_day16(self):
        self.assertEqual(day16.hex_to_bin("D2FE28"),"110100101111111000101000")
        v,l,p = day16.parse_packet("110100101111111000101000")
        self.assertEqual((v,l), (6,21))
        self.assertEqual(p[0].eval(),2021)

        v,l,p = day16.parse_packet(day16.hex_to_bin("38006F45291200"))
        self.assertEqual(v,p[0].sum_versions())
        self.assertEqual((v,l),(9,49))

        v,l,p = day16.parse_packet(day16.hex_to_bin("EE00D40C823060"))
        self.assertEqual(v,p[0].sum_versions())
        self.assertEqual((v,l),(14,51))

        v,l,p = day16.parse_packet(day16.hex_to_bin("C200B40A82"))
        self.assertEqual(p[0].eval(),3)

        tests = {"04005AC33890": 54, "880086C3E88112": 7, "CE00C43D881120": 9, "D8005AC2A8F0": 1, "F600BC2D8F": 0, "9C005AC2F8F0": 0, "9C0141080250320F1802104A08": 1}
        for h in tests.keys():
            v,l,p = day16.parse_packet(day16.hex_to_bin(h))
            self.assertEqual(p[0].eval(),tests[h])

        self.assertEqual(day16.part1("./data/day16_test.txt"),"31")

    def test_day17(self):
        with open("./data/day17_test2.txt") as f:
            path_lines = f.read().splitlines()
        paths = []
        for path in path_lines:
            paths.append((path.split(", ")[0],path.split(", ")[1]))

        self.assertEqual(day17.get_target_area("target area: x=20..30, y=-10..-5"),(20,30,-10,-5))
        p = day17.get_path(7,2,"target area: x=20..30, y=-10..-5")
        print("Path {}".format(p))
        self.assertTrue(day17.test_path(p,"target area: x=20..30, y=-10..-5"))
        p = day17.get_path(6,3,"target area: x=20..30, y=-10..-5")
        print("Path {}".format(p))
        self.assertTrue(day17.test_path(p,"target area: x=20..30, y=-10..-5"))
        p = day17.get_path(7,-1,"target area: x=20..30, y=-10..-5")
        print("Path {}".format(p))
        self.assertTrue(day17.test_path(p,"target area: x=20..30, y=-10..-5"))

        p = day17.get_path(6,0,"target area: x=20..30, y=-10..-5")
        print("Path {}".format(p))
        self.assertTrue(day17.test_path(p,"target area: x=20..30, y=-10..-5"))

        self.assertEqual(day17.part1("./data/day17_test.txt"),"45")
        answer_paths = day17.part2("./data/day17_test.txt")
        for p in paths:
            if not p in answer_paths:
                print("Missing {}".format(p))
        self.assertEqual(len(day17.part2("./data/day17_test.txt")),112)

    def test_day18(self):
        self.assertEqual(day18.add_nums("[1,1]","[2,2]"),"[[1,1],[2,2]]")
        result = day18.reduce("[[[[[9,8],1],2],3],4]")
        self.assertEqual(result,"[[[[0,9],2],3],4]")
        result = day18.reduce("[7,[6,[5,[4,[3,2]]]]]")
        self.assertEqual(result,"[7,[6,[5,[7,0]]]]")
        result = day18.reduce("[[6,[5,[4,[3,2]]]],1]")
        self.assertEqual(result,"[[6,[5,[7,0]]],3]")
        result = day18.reduce("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
        self.assertEqual(result,"[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        result = day18.split_num("[[[[0,7],4],[15,[0,13]]],[1,1]]")
        self.assertEqual(result,"[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
        self.assertEqual(day18.part1("./data/day18_test.txt"),4140)

        self.assertEqual(day18.magnitude("[9,1]"),29)
        self.assertEqual(day18.magnitude("[1,9]"), 21)
        self.assertEqual(day18.magnitude("[[9,1],[1,9]]"),129)
        self.assertEqual(day18.magnitude("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),1384)
        self.assertEqual(day18.magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"), 3488)

        self.assertEqual(day18.part2("./data/day18_test.txt"), 3993)

    def test_day19(self):
        self.assertEqual(day19.part1("./data/day19_test.txt"), "79")


if __name__ == '__main__':
    unittest.main()
