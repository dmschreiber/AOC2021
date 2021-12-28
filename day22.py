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

def find_overlap(p1,p2, state1, state2):
    ((x1,x2),(y1,y2),(z1,z2)) = p1
    ((x3,x4),(y3,y4),(z3,z4)) = p2

    # first include the second
    # wrong - this should split into a smaller one with state2 leaving the rest in state1
    if x1 < x3 and x2 > x4 and y1 < y3 and y2 > y4 and z1 < z3 and z2 > z4:
        if state1 == state2:
            yield ((x1,x2),(y1,y2),(z1,z2)), state1
        elif state2 == "on":
            yield p2, state2
        else:
            RuntimeError("shold explode something I'm not")

    # second includes the first
    elif x3 < x1 and x4 > x2 and y3 < y1 and y4 > y2 and z3 < z1 and z4 > z2:
        yield ((x3,x4),(y3,y4),(z3,z4)), state2

    # one point inside
    elif x1 >= x3 and x1 <= x4 and y1 >= y3 and y1 <= y4 and z1 >= z3 and z1 <= z4:
        print("one point inside {} {}".format(p1,p2))
        yield ((x1,x4),(y1,y4),(z1,z4)), state2 # overlap

        # split (x1,x2),(y1,y2),(z1,z2) by x4,y4,z4
        yield ((x1,x4),(y1,y4),(z4+1,z2)), state1 # above the overlap

        yield ((x4+1,x2),(y4+1,y2),  (z4+1,z2)), state1
        yield ((x4+1,x2),(y4+1,y2),  (z1,z4)), state1
        yield ((x1,x4),  (y4+1,y2),  (z4+1,z2)), state1
        yield ((x1, x4), (y4+1, y2), (z1, z4)), state1
        yield ((x4+1, x2), (y1,y4),  (z4+1,z2)), state1
        yield ((x4+1, x2), (y1, y4), (z1, z4)), state1


        # split (x3,x4),(y3,y4),(z3,z4) by x1,y1,z1
        yield ((x1+1,x4),(y1+1,y4),(z3,z1)), state2 #below the overlap
        yield ((x3,x1),(y3,y1),   (z3,z1)), state2
        yield ((x3,x1),(y3,y1),   (z1+1,z4)), state2
        yield ((x3,x1),(y1+1,y4),  (z3,z1)), state2
        yield ((x3, x1), (y1+1, y4), (z1+1, z4)), state2
        yield ((x1+1,x4),(y3,y1),(z3,z1)), state2
        yield ((x1+1, x4), (y3, y1), (z1+1, z4)), state2

    elif x2 >= x3 and x2 <= x4 and y2 >= y3 and y2 <= y4 and z2 >= z3 and z2 <= z4:
        print("one point inside {} {}".format(p1,p2))

        yield ((x3,x2),(y3,y2),(z3,z2)), state2 # overlap

        # split (x3,x4),(y3,y4),(z3,z4) by x2,y2,z2
        # 7 others
        yield ((x3,x2), (y3,y2),   (z2+1,z4)), state2 # above the overlap
        yield ((x3,x2), (y2+1,y4), (z2+1,z4)), state2
        yield ((x3,x2), (y2+1,y4), (z3,z2)), state2
        yield ((x2+1,x4), (y3,y2), (z2+1,z4)), state2
        yield ((x2+1,x4), (y3,y2), (z3,z2)), state2
        yield ((x2+1,x4), (y2+1,y4), (z2+1,z4)), state2
        yield ((x2+1,x4), (y2+1,y4), (z3,z2)), state2

        #split (x1,x2),(y1,y2),(z1,z2) by x3,y3,z3
        # 7 others
        yield ((x3+1,x2),(y3+1,y2),(z1,z3)), state1 # below the overlap
        yield ((x1,x3),(y1,y3),(z1,z3)), state1
        yield ((x1,x3),(y1,y3),(z3+1,z2)), state1
        yield ((x1,x3),(y3+1,y2),(z1,z3)), state1
        yield ((x1,x3),(y3+1,y2),(z3+1,z2)), state1
        yield ((x3+1,x2),(y1,y3),(z1,z3)), state1
        yield ((x3+1,x2),(y1,y3),(z3+1,z2)), state1

    else:
        yield p1, state1
        yield p2, state2

def calculate_volume(p):
    ((x1, x2), (y1, y2), (z1, z2)) = p
    return (abs(x2-x1)+1) * (abs(y2-y1)+1) * (abs(z2-z1)+1)


def part2(input):

    return str(other_part2(input))

    instructions = load_input(input)
    current_state = {}

    instruction_count = 0
    for p1, state1 in instructions.items():
        instruction_count += 1
        print("processing {} {}".format(p1,state1))

        new_state = {}
        if len(current_state) > 0 :
            for p2, state2 in current_state.items():
                for (new_cube, new_cube_state) in find_overlap(p2, p1, state2, state1):
                    if new_cube not in new_state.keys():
                        new_state[new_cube] = new_cube_state
        else:
            new_state[p1] = state1

        current_state = new_state
        print("Current state size {}".format(len(current_state)))

    v = 0
    for p,s in current_state.items():
        if s == "on":
            v += calculate_volume(p)
    print("Volume: {}".format(v))

    count = 0

    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                if check_map_strict(current_state, x, y, z) == "on":
                    count += 1

    return(str(count))

import re
from dataclasses import dataclass

@dataclass
class Transform3D:
    x: Tuple[int, int]
    y: Tuple[int, int]
    z: Tuple[int, int]

    @property
    def as_list(self) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        return self.x, self.y, self.z

    @property
    def inverse(self) -> Transform3D:
        return Transform3D(*[{
            n: (i, d)
            for i, (n, d) in enumerate(self.as_list)
        }[j] for j in range(3)])

@dataclass
class Point3D:
    x: int = 0
    y: int = 0
    z: int = 0

    @property
    def as_list(self) -> Tuple[int, int, int]:
        return self.x, self.y, self.z

    @property
    def manhattan_length(self) -> int:
        p = abs(self)
        return p.x + p.y + p.z

    def __abs__(self) -> Point3D:
        return Point3D(abs(self.x), abs(self.y), abs(self.z))

    def __hash__(self) -> int:
        return hash(self.as_list)

    def __eq__(self, other) -> bool:
        return self.as_list == other.as_list

    def __add__(self, other: Point3D) -> Point3D:
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Point3D) -> Point3D:
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    @property
    def volume(self) -> int:
        return self.x * self.y * self.z

    def cross(self, other: Point3D):
        return Point3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def transform(self, transformation: Transform3D) -> Point3D:
        coords = self.as_list
        return Point3D(*(coords[i] * n for i, n in transformation.as_list))

    def min(self, other: Point3D):
        return Point3D(
            min(self.x, other.x),
            min(self.y, other.y),
            min(self.z, other.z),
        )

    def max(self, other: Point3D):
        return Point3D(
            max(self.x, other.x),
            max(self.y, other.y),
            max(self.z, other.z),
        )

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'


class Cube:
    def __init__(self, p_min: Point3D, p_max: Point3D, state: int = 1):
        self.p_min = p_min
        self.p_max = p_min.max(p_max)
        self.state = state

    @property
    def volume(self) -> int:
        return (self.p_max - self.p_min).volume * self.state

    def __and__(self, other: Cube) -> Cube:
        return Cube(self.p_min.max(other.p_min), self.p_max.min(other.p_max), -other.state)

    def __contains__(self, other: Cube) -> bool:
        return other == self & other

    def __eq__(self, other: Cube) -> bool:
        return self.p_min == other.p_min and self.p_max == other.p_max

    def __bool__(self) -> bool:
        return self.volume != 0


def parse_input(input_lines: List[str], init_mode: bool = False) -> List[Cube]:
    return [cube for line in input_lines if (cube := Cube(
        *[Point3D(x, y, z) for x, y, z in zip(*[
            (int(a), int(b) + 1)
            for a, b in re.findall(r'[xyz]=(-?\d+)..(-?\d+)', line)
        ])],
        state=1 if line.startswith('on') else -1,
    )) in Cube(Point3D(-50, -50, -50), Point3D(50, 50, 50)) or not init_mode]


def count_on_states(input_cubes: List[Cube]) -> int:
    cubes: List[Cube] = []
    for cube in input_cubes:
        cubes += [intersection for c in cubes if (intersection := cube & c)]
        if cube.state == 1:
            cubes.append(cube)
    return sum(cube.volume for cube in cubes)


def other_part2(input) -> int:
    with open(input) as f:
        input_lines = f.read().splitlines()

    return count_on_states(parse_input(input_lines))
