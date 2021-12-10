def is_lowest(map, i, j):
    if i>0 :
        if map[i][j] >= map[i-1][j] :
            return False

    if j>0:
        if map[i][j] >= map[i][j-1] :
            return False

    if i<len(map)-1:
        if map[i][j] >= map[i+1][j] :
            return False

    if j<len(map[i])-1 :
        if map[i][j] >= map[i][j+1] :
            return False

    return True

def print_map(map):
    for i in range(len(map)) :
        for j in range(len(map[i])) :
            if is_lowest(map, i, j) :
                print("[{}]".format(map[i][j]), end="")
            else  :
                print(" {} ".format(map[i][j]), end="")
        print("")

def read_map(input_lines):
    map = {}

    for i in range(len(input_lines)) :
        map[i] = [int(x) for x in list(input_lines[i])]
    return map

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = read_map(input_lines)
    total = 0

    for i in range(len(map)) :
        for j in range(len(map[i])) :
            if is_lowest(map, i, j) :
                total = total + map[i][j] + 1

    return str(total)

def sum_basin(map, i, j):
    size = 0
    points = []
    if i< 0 or j<0 or i>=len(map) or j>=len(map[i]) :
        return points

    if i>0 :
        if map[i][j] < map[i-1][j]  and map[i-1][j] != 9 :
            points.extend(sum_basin(map, i-1, j))

    if j>0:
        if map[i][j] < map[i][j-1] and map[i][j-1] != 9 :
            points.extend(sum_basin(map, i, j-1))

    if i<len(map)-1:
        if map[i][j] < map[i+1][j] and map[i+1][j] != 9 :
            points.extend(sum_basin(map, i+1, j))

    if j<len(map[i])-1 :
        if map[i][j] < map[i][j+1] and map[i][j+1] != 9 :
            points.extend(sum_basin(map, i, j+1))

    points.append((i,j))
    return list(dict.fromkeys(points))

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = read_map(input_lines)
    low_points = {}

    for i in range(len(map)) :
        for j in range(len(map[i])) :
            if is_lowest(map, i, j) :
#                print("Low point {},{}" .format(i,j))
                low_points[(i,j)] = sum_basin(map, i, j)

    sizes = [len(l) for l in low_points.values()]
    sizes.sort(reverse=True)

#    for k, v in low_points.items() :
#        print("{} : {}".format(k, len(v)))

#   print("Sizes {}".format(sizes))
    return str(sizes[0]*sizes[1]*sizes[2])