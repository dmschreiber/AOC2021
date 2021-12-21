import re


def get_target_area(input_line):
    pattern_text = r'^target area: x=(?P<min_x>-?\d+)..(?P<max_x>-?\d+), y=(?P<min_y>-?\d+)..(?P<max_y>-?\d+)$'
    pattern = re.compile(pattern_text)
    match = pattern.match(input_line)
    if match==None:
        print("Error: input line does not match pattern ({} vs {})".format(input_line,pattern_text))
        return None
    return int(match.group("min_x")), int(match.group("max_x")), int(match.group("min_y")), int(match.group("max_y"))

def test_path(points, target_area):
    min_x, max_x, min_y, max_y = get_target_area(target_area)
    for x,y in points:
        if x>=min_x and x<=max_x and y>=min_y and y<=max_y:
            return True
    return False


def get_path(v_x, v_y, target_area):
    # target area: x=20..30, y=-10..-5
#     print("Test velocity {}".format((v_x,v_y)))
    points = [(0,0)]
    min_x, max_x, min_y, max_y = get_target_area(target_area)
    x = 0
    y = 0
    while (x <= max_x and y >= min_y):
        x += v_x
        y += v_y
        if v_x > 0:
            v_x -= 1
        elif v_x < 0:
            v_x += 1
        v_y -= 1
        points.append((x,y))
        if x>=min_x and x<max_x and y>=min_y and y<max_y:
            return points

    return points


def part1(input):
    with open(input) as f:
        target_area = f.read().splitlines()

    max_y = 0
    for v_x in range(-30,30):
        for v_y in range(-500,500):
            p = get_path(v_x, v_y, target_area[0])
            if test_path(p, target_area[0]):
                path_max_y = max([p[i][1] for i in range(len(p))])
                if path_max_y > max_y:
                    max_y = path_max_y
#                print("Found path {} max_y {}".format((v_x,v_y),path_max_y))

    return str(max_y)

def part2(input):
    with open(input) as f:
        target_area = f.read().splitlines()

    max_y = 0
    count = 0
    paths = []
    for v_x in range(0,178):
        for v_y in range(-107,150):
            p = get_path(v_x, v_y, target_area[0])
            if test_path(p, target_area[0]):
                path_max_y = max([p[i][1] for i in range(len(p))])
                if path_max_y > max_y:
                    max_y = path_max_y
                count +=1
                paths.append((str(v_x),str(v_y)))
#                print("Found path {} max_y {}".format((v_x,v_y),path_max_y))
# 402 is too low
    # 858 too low
    # 2082 too low
    return paths
