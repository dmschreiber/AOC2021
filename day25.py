import copy


def part1(input):
    map = load_map(input)

    count = 0
    last_map = []


    while stringify(map) != stringify(last_map):
        count += 1
        last_map = map
        map = perform_step(map)

    return(count)

def stringify(map):
    return "".join(map[i][j] for i in range(len(map)) for j in range(len(map[i])))


def load_map(input):
    with open(input) as f:
        input_lines = f.read().splitlines()
    map = []
    for line in input_lines:
        map.append(list(line))
    return map


def get_right(map, row, col):
    target_col = (col+1) % len(map[row])
    return map[row][target_col]


def get_south(map, row, col):
    target_row = (row+1) % len(map)
    return map[target_row][col]


def move_right(map, row, col):
    target_col = (col+1) % len(map[row])
    map[row][target_col] = map[row][col]
    map[row][col] = '.'


def move_south(map, row, col):
    target_row = (row+1) % len(map)
    map[target_row][col] = map[row][col]
    map[row][col] = '.'


def perform_step(map):

    new_map = []
    for i in range(len(map)):
        new_map.append(map[i].copy())

    # east-facing herd
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '>' and get_right(map,i,j) == '.':
                move_right(new_map,i,j)

    # south-facing herd
    map = new_map
    new_map = []
    for i in range(len(map)):
        new_map.append(map[i].copy())

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'v' and get_south(map,i,j) == '.':
                move_south(new_map,i,j)

    return new_map


def print_map(map):
    for line in map:
        print(''.join(line))


def part2(input):
    with open(input) as f:
        depths = f.read().splitlines()
    count = 0



    return(str(count))
