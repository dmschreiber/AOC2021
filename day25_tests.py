import unittest
import time
import copy
import day25


initial_state = "v...>>.vv>.vv>>.vv..>>.>v>...v>>v>>.>.v.v>v.vv.v..>.>>..v....vv..>.>v.v.v..>>v.v....v..v.>"
after_step_1 =  "....>.>v.>v.v>.>v.v.>v>>..>v..>>v>v>.>.v.>v.v...v.v>>.>vvv....v...>>..vv...>>vv.>.v.v..v.v"
after_step_20 = "v>.....>>.>vv>.....v.>v>v.vv>>v>>>v.>v.>....vv>v...v.>>>vvv...v..>>vv.v.v...>>.v..v.....v>"

class MyTestCase(unittest.TestCase):
    def test_day25(self):
        map = day25.load_map("./data/day25_test.txt")
        self.assertEqual((day25.stringify(map)),initial_state)

        map = day25.perform_step(map)
        self.assertEqual(("".join(map[i][j] for i in range(len(map)) for j in range(len(map[i])))),after_step_1)

        for i in range(19):
            map = day25.perform_step(map)

        self.assertEqual(("".join(map[i][j] for i in range(len(map)) for j in range(len(map[i])))),after_step_20)

        map = day25.load_map("./data/day25_test.txt")
        for i in range(55):
            map = day25.perform_step(map)

        last_map = []
        for i in range(4):
            last_map = copy.deepcopy(map)
            print("after Step {}".format(i+55))
            day25.print_map(map)
            map = day25.perform_step(map)

        self.assertEqual(day25.stringify(map),day25.stringify(last_map))

        print("Solving for first step where nobody moves")
        map = day25.load_map("./data/day25_test.txt")
        self.assertEqual(day25.part1("./data/day25_test.txt"),58)

if __name__ == '__main__':
    unittest.main()
