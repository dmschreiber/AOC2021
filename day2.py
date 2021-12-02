def part1(input):
    with open(input) as f:
        directions = f.read().splitlines()

    horiz = 0
    vert = 0

    for item in directions:
        (direction,units) = item.split()
        print("{}:{}".format(direction,units))
        if direction == "forward":
            horiz = horiz + int(units)

        if direction == "up":
            vert = vert - int(units)

        if direction == "down":
            vert = vert + int(units)




    return(str(horiz*vert))

def part2(input):
    with open(input) as f:
        directions = f.read().splitlines()

    aim = 0
    horiz = 0
    vert = 0

    for item in directions:
        (direction,units) = item.split()

        if direction == "up":
            aim = aim - int(units)

        if direction == "down":
            aim = aim + int(units)

        if direction == "forward":
            horiz = horiz + int(units)
            vert = vert + aim*int(units)

    return(str(horiz*vert))