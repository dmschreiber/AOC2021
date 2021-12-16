from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def get_neighbors(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


def create_map(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = []
    row = 0
    for line in input_lines:
        map.append([int(l) for l in list(line)])
        row += 1
    return map


def create_part2_map(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = []
    row = 0
    for line in input_lines:
        map.append([int(l) for l in list(line)])
        for offset in range(1,5):
            map[row].extend([(map[row][((offset-1)*len(line)+i)]+1) % 10 if (map[row][((offset-1)*len(line)+i)] + 1) % 10 > 0 else 1 for i in range(len(line))])

#        map[row].extend([(int(l)+1)%10 if (int(l)+1)%10 > 0 else 1 for l in list(line)])
#        map[row].extend([(int(l)+2)%10 if (int(l)+2)%10 > 0 else 1 for l in list(line)])
#        map[row].extend([(int(l)+3)%10 if (int(l)+3)%10 > 0 else 1 for l in list(line)])
#        map[row].extend([(int(l)+4)%10 if (int(l)+4)%10 > 0 else 1 for l in list(line)])
        row += 1

    for j in range(len(input_lines)):
        for offset in range(1,5):
            map.append([(map[row-len(input_lines)][i]+1)%10 if (map[row-len(input_lines)][i]+1)%10>0 else 1 for i in range(len(map[0]))])
            row += 1

#        map.append([(int(l)+1)%10 if (int(l)+1)%10 >0 else 1 for l in map[j]])
#        map.append([(int(l)+1)%10 if (int(l)+2)%10 >0 else 1 for l in map[j]])
#        map.append([(int(l)+1)%10 if (int(l)+3)%10 >0 else 1 for l in map[j]])
#        map.append([(int(l)+1)%10 if (int(l)+4)%10 >0 else 1 for l in map[j]])

    return map


def part1(input):
    map = create_map(input)

    grid = Grid(matrix=map)

    start = grid.node(0,0)
    end = grid.node(len(map[0])-1,len(map)-1)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path,runs = finder.find_path(start, end, grid)

    print(path)
    count = 0
    for i in range(1,len(path)):
        count += map[path[i][1]][path[i][0]]

    return(str(count))

def part2(input):
    with open(input) as f:
        depths = f.read().splitlines()
    count = 0

    map = create_part2_map(input)
    if (False):
        for j in range(len(map)):
            for i in range(len(map[j])):
                print(map[j][i], end="")
            print()
    grid = Grid(matrix=map)

    start = grid.node(0,0)
    end = grid.node(len(map[0])-1,len(map)-1)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path,runs = finder.find_path(start, end, grid)

    print(path)
    count = 0
    for i in range(1,len(path)):
        count += map[path[i][1]][path[i][0]]

    return(str(count))

    return(str(count))
