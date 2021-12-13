import re

O = [["#####"],
     ["#   #"],
     ["#   #"],
     ["#   #"],
     ["#####"]]

def fold_map(old_map, orientation, number):
    new_map = {}

    if orientation == "y":
        for spot in old_map.keys():
            if spot[1] < number:
                new_map[(spot[0], spot[1])] = old_map[(spot[0], spot[1])]

        for spot in old_map.keys():
            if spot[1] > number:
                new_y = number - (spot[1] - number)
                new_map[(spot[0], new_y)] = old_map[(spot[0], spot[1])] or new_map[(spot[0], spot[1])]

    elif orientation == "x":
        for spot in old_map.keys():
            if spot[0] < number:
                new_map[(spot[0], spot[1])] = old_map[(spot[0], spot[1])]

        for spot in old_map.keys():
            if spot[0] > number:
                new_x = number - (spot[0] - number)
                new_map[(new_x, spot[1])] = old_map[(spot[0], spot[1])] or new_map[(spot[0], spot[1])]

    return new_map

def read_and_fold(input, fold_count = None):
    with open(input) as f:
        lines = f.read().splitlines()

    folds = []
    map = {}

    for line in lines :
        if "fold" in line:
            folds.append(line)
        elif line != "":
            x = int(line.split(",")[0])
            y = int(line.split(",")[1])
            map[(x,y)] = True

    if fold_count is None:
        fold_count = len(folds)

    for i in range(fold_count):
        pattern_text = r'^fold along (?P<axis>[x|y])=(?P<number>\d+)$'
        pattern = re.compile(pattern_text)
        match = pattern.match(folds[i])
        print("Fold on {}={}".format(match.group("axis"),match.group("number")))

        map = fold_map(map, match.group("axis"), int(match.group("number")))

    return map


def part1(input):
    map = read_and_fold(input, 1)
    count = sum([1 for l in map.values() if l])

    return(str(count))

def part2(input):
    map = read_and_fold(input)

    x_list = [spot[0] for spot in map.keys()]
    y_list = [spot[1] for spot in map.keys()]
    max_x = max(x_list)
    max_y = max(y_list)
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in map.keys() and map[(x,y)]:
                print("#", end="")
            else:
                print(" ", end="")
        print("")

    return ""
