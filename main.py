import time
import day1
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

if __name__ == '__main__':
    day1_input = "./data/day1.txt"
    print("Day 1 part 1:" + day1.part1(day1_input))
    print("Day 1 part 2:" + day1.part2(day1_input))

    day2_input = "./data/day2.txt"
    print("Day 2 part 1:" + day2.part1(day2_input))
    print("Day 2 part 2:" + day2.part2(day2_input))

    day3_input = "./data/day3.txt"
    print("Day 3 part 2:" + day3.part2(day3_input))
    print("Day 3 part 1:" + day3.part1(day3_input))

    day4_input = "./data/day4.txt"
    print("Day 4 part 1:" + day4.part1(day4_input))
    print("Day 4 part 2:" + day4.part2(day4_input))

    day5_input = "./data/day5.txt"
    print("Day 5 part 1:" + day5.part1(day5_input))
    print("Day 5 part 2:" + day5.part2(day5_input))

    day6_input = "./data/day6.txt"
    print("Day 6 part 1:" + day6.part2(day6_input,80))
    print("Day 6 part 2:" + day6.part2(day6_input,256))

    day7_input = "./data/day7.txt"
    print("Day 7 part 1:" + day7.part1(day7_input))
    print("Day 7 part 2:" + day7.part2(day7_input))

    day8_input = "./data/day8.txt"
    print("Day 8 part 1:" + day8.part1(day8_input))
    print("Day 8 part 2:" + day8.part2(day8_input))

    day9_input = "./data/day9.txt"
    print("Day 9 part 1:" + day9.part1(day9_input))
    print("Day 9 part 2:" + day9.part2(day9_input))

    day10_input = "./data/day10.txt"
    print("Day 10 part 1:" + day10.part1(day10_input))
    print("Day 10 part 2:" + day10.part2(day10_input))

    day11_input = "./data/day11.txt"
    print("Day 11 part 1:" + day11.part1(day11_input))
    print("Day 11 part 2:" + day11.part2(day11_input))

    start_time = time.perf_counter()
    day12_input = "./data/day12.txt"
    print("Day 12 part 1:" + day12.part1(day12_input))
    print("Day 12 part 2:" + day12.part2(day12_input))
    end_time = time.perf_counter()
    print(f"Day 12 execution Time : {end_time - start_time:0.6f}s")

    day13_input = "./data/day13.txt"
    print("Day 13 part 1:" + day13.part1(day13_input))
    print("Day 13 part 2:" + day13.part2(day13_input))

    day14_input = "./data/day14.txt"
    print("Day 14 part 1:" + day14.part1(day14_input))
    print("Day 14 part 2:" + day14.part2(day14_input))

    day15_input = "./data/day15.txt"
    start_time = time.perf_counter()
    print("Day 15 part 1:" + day15.part1(day15_input))
    #long exec time
    #print("Day 15 part 2:" + day15.part2(day15_input))
    end_time = time.perf_counter()
    print(f"Day 15 execution Time : {end_time - start_time:0.6f}s")

    day16_input = "./data/day16.txt"
    print("Day 16 part 1:" + day16.part1(day16_input))
    print("Day 16 part 2:" + day16.part2(day16_input))

    day17_input = "./data/day17.txt"
    print("Day 17 part 1:" + day17.part1(day17_input))
    print("Day 17 part 2: {}".format(len(day17.part2(day17_input))))
