def read_map(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = {}

    for i in range(len(input_lines)) :
        map[i] = [int(x) for x in list(input_lines[i])]
    return map

def print_map(map):
    for i in range(len(map)) :
        print("".join([str(s) for s in map[i]]))

def process(map, i, j) :
    flashes = 0

    if map[i][j] > 9 :
        flashes += 1
        map[i][j] = 0

        if i > 0 :
            if j > 0 :
                if map[i-1][j-1] != 0 :
                    map[i-1][j-1] += 1
            if map[i-1][j] != 0 :
                map[i-1][j] += 1

            if j < len(map[i]) - 1 :
                if map[i-1][j+1] != 0 :
                    map[i-1][j+1] += 1

        if j > 0 :
            if map[i][j-1] != 0 :
                map[i][j-1] += 1
        if j < len(map[i]) - 1 :
            if map[i][j+1] != 0 :
                map[i][j+1] += 1
        if i < len(map) - 1 :
            if j > 0 :
                if map[i+1][j-1] != 0 :
                    map[i+1][j-1] += 1
            if map[i+1][j] != 0 :
                map[i+1][j] += 1
            if j < len(map[i]) - 1 :
                if map[i+1][j+1] != 0 :
                    map[i+1][j+1] += 1

    return (map,flashes)

def step(map, count) :
    total_flashes = 0
    new_map = map.copy()


    for i in range(len(new_map)) :
        for j in range(len(new_map[i])) :
            new_map[i][j] += 1

    new_count = 1

    while new_count > 0 :
        new_count = 0
        for i in range(len(new_map)):
            for j in range(len(new_map[i])):
#                print("process {},{}".format(i,j))
                (new_map,flashes) = process(new_map, i, j)
                new_count += flashes
#        print("{} Flashes this time {} so far".format(new_count, total_flashes))

        total_flashes += new_count


    return (new_map, total_flashes + count)

def part1(input):

    map = read_map(input)
    count = 0

    for i in range(100) :
        (map, count) = step(map, count)

    print("Total Flashes: {}".format(count))
    return(str(count))

def part2(input):
    map = read_map(input)
    count = 0
    map = read_map(input)
    count = 0
    last_count = 0
    step_count = 0

    while (count - last_count) != 100 :
        last_count = count
        (map, count) = step(map, count)
        step_count = step_count + 1

    print("All squids flashed: {}".format(step_count))

    return(str(step_count))
