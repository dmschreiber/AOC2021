def part1(input):
    return generalized(input, True)

def part2(input):
    return generalized(input, False)

def generalized(input, only_horizvert):
    with open(input) as f:
        input_lines = f.read().splitlines()

    lines = [line.split(" -> ") for line in input_lines]
    lines = [(line[0].split(","), line[1].split(",")) for line in lines]

    if only_horizvert:
        lines = [line for line in lines if (line[0][0] == line[1][0] or line[0][1] == line[1][1])]

    map = {}

    for line in lines:
        x1 = int(line[0][0])
        y1 = int(line[0][1])
        x2 = int(line[1][0])
        y2 = int(line[1][1])

        if x1 <= x2 :
            x_step = 1
        else:
            x_step = -1

        if y1 <= y2 :
            y_step = 1
        else:
            y_step = -1

        if x1 == x2 or y1 == y2:
            for x in range(x1,x2+x_step,x_step):
                for y in range(y1,y2+y_step, y_step):
                    key = "{},{}".format(x,y)
                    if key in map :
                        map[key] = map[key] + 1
                    else:
                        map[key] = 1
        else:
#            print("Diag {},{} -> {},{}".format(x1,y1,x2,y2))
            x = x1
            y = y1
            for i in range(x1,x2+x_step,x_step):
                key = "{},{}".format(x, y)
                if key in map:
                    map[key] = map[key] + 1
                else:
                    map[key] = 1
                x = x + x_step
                y = y + y_step

    intersections = len([point for point in map.values() if point > 1])
    # print("There are {} intersections".format(intersections))
    return str(intersections)

# part 2 19748 is too low
