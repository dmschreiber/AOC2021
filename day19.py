import re
import itertools
import time


def transform(scanner):

    for x in (1,-1):
        for y in (1,-1):
            for z in (1,-1):
                yield([(p[0]*x,p[1]*y,p[2]*z) for p in scanner])
                yield([(p[0]*x,p[2]*z,p[1]*y) for p in scanner])
                yield([(p[2]*z,p[0]*x,p[1]*y) for p in scanner])
                yield([(p[2]*z,p[1]*y,p[0]*x) for p in scanner])
                yield([(p[1]*y,p[2]*z,p[0]*x) for p in scanner])
                yield([(p[1]*y,p[0]*x,p[2]*z) for p in scanner])


def calculate_pairs(scanner):
    pairs = list(itertools.combinations(scanner,2))

#    pair_differences = [(p[0][0]-p[1][0],p[0][1]-p[1][1],p[0][2]-p[1][2]) for p in pairs]

    return pairs

def create_matches(pairs1, pairs2):
    matched_pairs = []
    matched_points = []


    for p in pairs1:
        for q in pairs2:
            if (p[0][0] - p[1][0], p[0][1] - p[1][1], p[0][2] - p[1][2]) == (q[0][0] - q[1][0], q[0][1] - q[1][1], q[0][2] - q[1][2]):
                matched_pairs.append( (p,q) )
    # a,b matching y,z
    # if a,n matches y,(anything else)
    for m in matched_pairs:
        left_first_point = m[0][0]
        left_second_point = m[0][1]
        right_first_point = m[1][0]
        right_second_point = m[1][1]

        for n in matched_pairs:
            if n[0][0] == left_second_point and n[0][1] != left_first_point:
                if right_first_point == n[1][0] and (left_second_point, n[1][0]) not in matched_points :
                    matched_points.append((left_second_point, n[1][0]))
                if right_first_point == n[1][1] and (left_second_point, n[1][1]) not in matched_points:
                    matched_points.append((left_second_point, n[1][1]))
                if right_second_point == n[1][0] and (left_second_point, n[1][0]) not in matched_points:
                    matched_points.append((left_second_point, n[1][0]))
                if right_second_point == n[1][1] and (left_second_point, n[1][1]) not in matched_points:
                    matched_points.append((left_second_point, n[1][1]))
            if n[0][0] == left_first_point and n[0][1] != left_second_point:
                if right_first_point == n[1][0] and (left_first_point, n[1][0]) not in matched_points :
                    matched_points.append((left_first_point, n[1][0]))
                if right_first_point == n[1][1] and (left_first_point, n[1][1]) not in matched_points:
                    matched_points.append((left_first_point, n[1][1]))
                if right_second_point == n[1][0] and (left_first_point, n[1][0]) not in matched_points:
                    matched_points.append((left_first_point, n[1][0]))
                if right_second_point == n[1][1] and (left_first_point, n[1][1]) not in matched_points:
                    matched_points.append((left_first_point, n[1][1]))
            if n[0][1] == left_second_point and n[0][0] != left_first_point:
                if right_first_point == n[1][0] and (left_second_point, n[1][0]) not in matched_points :
                    matched_points.append((left_second_point, n[1][0]))
                if right_first_point == n[1][1] and (left_second_point, n[1][1]) not in matched_points :
                    matched_points.append((left_second_point, n[1][1]))
                if right_second_point == n[1][0] and (left_second_point, n[1][0]) not in matched_points:
                    matched_points.append((left_second_point, n[1][0]))
                if right_second_point == n[1][1] and (left_second_point, n[1][1]) not in matched_points:
                    matched_points.append((left_second_point, n[1][1]))
            if n[0][1] == left_first_point and n[0][0] != left_second_point:
                if right_first_point == n[1][0] and (left_first_point, n[1][0]) not in matched_points :
                    matched_points.append((left_first_point, n[1][0]))
                if right_first_point == n[1][1] and (left_first_point, n[1][1]) not in matched_points :
                    matched_points.append((left_first_point, n[1][1]))
                if right_second_point == n[1][0] and (left_first_point, n[1][0]) not in matched_points:
                    matched_points.append((left_first_point, n[1][0]))
                if right_second_point == n[1][1] and (left_first_point, n[1][1]) not in matched_points:
                    matched_points.append((left_first_point, n[1][1]))
            if n[0][1] == left_first_point and n[0][0] == left_second_point:
                if (left_first_point,n[1][0]) in matched_points:
                    matched_points.append((left_second_point,n[1][1]))
                if (left_second_point, n[1][1]) in matched_points:
                    matched_points.append((left_first_point, n[1][0]))
            if n[0][0] == left_first_point and n[0][1] == left_second_point:
                if (left_first_point,n[1][1]) in matched_points and (left_second_point,n[1][0]) not in matched_points:
                    matched_points.append((left_second_point,n[1][0]))
                if (left_second_point, n[1][0]) in matched_points and (left_first_point, n[1][1]) not in matched_points:
                    matched_points.append((left_first_point, n[1][1]))

    # print("{} Matched Points".format(len(matched_points)))

    items = [(p[0][0]-p[1][0],p[0][1]-p[1][1],p[0][2]-p[1][2]) for p in matched_points]
    frequ = {}
    for i in items:
        if i in frequ:
            frequ[i] += 1
        else:
            frequ[i] = 1
    if len(frequ) == 1:
        for f_k in frequ.keys():
            return f_k

    return None

def match_pairs(pairs1, pairs2):
    count = 0
    matched_points = []

    for p in pairs1:
        if (p[0][0] - p[1][0], p[0][1] - p[1][1], p[0][2] - p[1][2]) in [(q[0][0] - q[1][0], q[0][1] - q[1][1], q[0][2] - q[1][2]) for q in pairs2]:
            if p[0] not in matched_points:
                matched_points.append(p[0])
            if p[1] not in matched_points:
                matched_points.append(p[1])
        if (p[1][0] - p[0][0], p[1][1] - p[0][1], p[1][2] - p[0][2]) in [(q[0][0] - q[1][0], q[0][1] - q[1][1], q[0][2] - q[1][2]) for q in pairs2]:
            if p[0] not in matched_points:
                matched_points.append(p[0])
            if p[1] not in matched_points:
                matched_points.append(p[1])

    return len(matched_points)




def specific_transform(s,t):
    index = 0
    for which_transform in transform(s):
        if index == t:
            return which_transform
        index += 1


def read_in_scanners(input):
    with open(input) as f:
        input_lines = f.read().splitlines()
    scanners = []
    line_count = 0
    while line_count < len(input_lines):
        if re.match(r'^--- scanner (\d+) ---$', input_lines[line_count]):
            scanners.append([])
        elif re.match(r'^-?\d+,-?\d+,-?\d+', input_lines[line_count]):
            m = re.match(r'^(-?\d+),(-?\d+),(-?\d+)', input_lines[line_count])
            scanners[len(scanners) - 1].append([int(m.group(1)), int(m.group(2)), int(m.group(3))])
        line_count += 1
    return scanners


def map_to_zero(offset, target):

    if ((0,0),target) in offset.keys():
        return offset[(0,0),target]
    else:
        for mapping in offset:
            if target == (mapping[1][0],mapping[1][1]):
                interim = map_to_zero(offset,(mapping[0][0],mapping[0][1]))
                return (offset[mapping][0]+interim[0], offset[mapping][1]+interim[1], offset[mapping][2]+interim[2])


checked_scanners = []
def register_scanner(source,target):
    if (source,target) not in checked_scanners:
        checked_scanners.append((source,target))
    if (target,source) not in checked_scanners:
        checked_scanners.append((target,source))


def find_offset(offset, pairs, scanners,which_scanner):
    found_scanner = False

    if which_scanner == 0:
        i = 0
        t = 0
        found_scanner = True

    elif which_scanner in [o[1][0] for o in offset.keys()]:
        i = which_scanner
        t = [o[1][1] for o in offset.keys() if o[1][0] == which_scanner][0]
        found_scanner = True

    if found_scanner:
        # print("checking for matches with {}-{}".format(i,t))
        for j in range(len(scanners)):
            if i != j and j not in [mapping[1][0] for mapping in offset.keys()]:
                for u in range(len(pairs[j])):
                    if ((i,t),(j,u)) not in checked_scanners:
                        register_scanner((i,t),(j,u))

                        p = create_matches(pairs[i][t], pairs[j][u])
                        if p is not None:
                            # print("Scanner {} t {} with scanner {} t {} is {}".format(i, t, j, u, p))

                            new_offset = offset.copy()
                            new_offset[ ((i,t),(j,u))] = p
                            yield ((i,t),(j,u)),p
                            if j not in [o[0][0] for o in offset.keys()]:
                                for n in find_offset(new_offset, pairs, scanners, j):
                                    yield n
                            break


def part1(input):
    scanners = read_in_scanners(input)

    count = len(scanners)
    scanner_index=0
    pairs = [] # one per scanner

    start_time = time.perf_counter()
    for s in scanners:
        pairs.append([])
        transform_count = 0
        for t in transform(s):
            pairs[scanner_index].append(calculate_pairs(t)) # a list of pairs for each of 24 transforms
            transform_count += 1

        scanner_index = scanner_index + 1
    end_time = time.perf_counter()
    print(f"Part 15.1 time : {end_time - start_time:0.6f}s")


    offset = {}
    for i_t_j_u, p in find_offset(offset, pairs, scanners, 0):
        offset[i_t_j_u] = p
    end_time = time.perf_counter()
    print(f"Part 15.2 time : {end_time - start_time:0.6f}s")

    points = [(p[0],p[1],p[2]) for p in scanners[0]]

    positions_of_scanners = {}
    positions_of_scanners[0] = (0,0,0)

    for mapping in offset.keys():
        target = (mapping[1][0],mapping[1][1])
        scanner_pos = map_to_zero(offset,target)
        positions_of_scanners[mapping[1][0]] = scanner_pos

        for p in [(p[0]+scanner_pos[0],p[1]+scanner_pos[1],p[2]+scanner_pos[2]) for p in specific_transform(scanners[mapping[1][0]],mapping[1][1])]:
            if p not in points:
                points.append(p)

    points.sort(key=lambda p: (p[0],p[1],p[2]))
    end_time = time.perf_counter()
    print(f"Part 15.3 time : {end_time - start_time:0.6f}s")

    biggest_manhattan_distance = 0

    for i in positions_of_scanners.values():
        for j in positions_of_scanners.values():
            distance = abs(i[0]-j[0])+abs(i[1]-j[1])+abs(i[2]-j[2])
            if distance > biggest_manhattan_distance:
                biggest_manhattan_distance = distance

    print("Biggest Manhattan Distance between scanners is {}".format(biggest_manhattan_distance))
    end_time = time.perf_counter()
    print(f"Part 15.4 time : {end_time - start_time:0.6f}s")

    return(str(len(points)))


def part2(input):
    with open(input) as f:
        depths = f.read().splitlines()
    count = 0



    return(str(count))
