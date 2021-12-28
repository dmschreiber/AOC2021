from __future__ import annotations
import re

from typing import Tuple, List


def load_input(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = {}
    pattern_text = r'^(?P<state>[onf]+) x=(?P<min_x>-?\d+)..(?P<max_x>-?\d+),y=(?P<min_y>-?\d+)..(?P<max_y>-?\d+),z=(?P<min_z>-?\d+)..(?P<max_z>-?\d+)$'
    pattern = re.compile(pattern_text)
    for l in input_lines:
        match = pattern.match(l)
        if match:
            map[((int(match.group('min_x')), int(match.group('max_x'))), (int(match.group('min_y')), (int(match.group('max_y')))), (int(match.group('min_z')),int(match.group('max_z'))))] = match.group("state")

    return map


def check_map(map, x, y, z):
    last_state = "off"
    for ((min_x, max_x), (min_y, max_y), (min_z, max_z)), state in map.items():
        if x >= min_x and x <= max_x and y >= min_y and y <= max_y and z >= min_z and z <= max_z:
            last_state = state

    return last_state

def check_map_strict(map, x, y, z):
    last_state = "off"
    count = 0
    for ((min_x, max_x), (min_y, max_y), (min_z, max_z)), state in map.items():
        if x >= min_x and x <= max_x and y >= min_y and y <= max_y and z >= min_z and z <= max_z:
            return state

def part1(input):
    instructions = load_input(input)

    count = 0

    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                if check_map(instructions, x, y, z) == "on":
                    count += 1



    return(str(count))

def find_min_max(p1, p2):
    ((x1,x2),(y1,y2),(z1,z2)) = p1
    ((x3,x4),(y3,y4),(z3,z4)) = p2


    result = ((max(x1,x3), min(x2,x4)),
              (max(y1,y3), min(y2,y4)),
              (max(z1,z3), min(z2,z4)))
    result = ((result[0][0], max(result[0][0],result[0][1])),
              (result[1][0], max(result[1][0],result[1][1])),
              (result[2][0], max(result[2][0],result[2][1])))
    return result


def is_empty(p1):
    return calculate_volume(p1) == 0


def find_overlap(p1,p2, state2):
    ((x1,x2),(y1,y2),(z1,z2)) = p1
    ((x3,x4),(y3,y4),(z3,z4)) = p2

    result = find_min_max(p1, p2)

    if not is_empty(result):
        return result, -state2


def calculate_volume(p):
    ((x1, x2), (y1, y2), (z1, z2)) = p
    return (abs(x2-x1)) * (abs(y2-y1)) * (abs(z2-z1))


def part2(input):

    instructions = load_input(input)
    current_state = []

    instruction_count = 0
    for p1, state1 in instructions.items():
        instruction_count += 1
        p1 = ((p1[0][0], p1[0][1]+1), (p1[1][0], p1[1][1]+1), (p1[2][0], p1[2][1]+1))
        # print("processing {} {}".format(p1,state1))
        new_adds = [o for p2, state2 in current_state if (o := find_overlap(p1, p2, state2))]
        # for s in new_adds:
        #     print("adding {}".format(s))

        current_state += new_adds

        if state1 == "on":
            current_state.append((p1, 1))

        # print("Current state size {}".format(len(current_state)))

    v = 0
    for p,s in current_state:
            v += calculate_volume(p)*s
    print("Volume: {}".format(v))

    count = v

    return(str(count))

