import string
import collections

def is_small(spot):
    if list(spot[0:1])[0] in list(string.ascii_lowercase):
        return True
    else:
        return False


def find_path(map, spot, path=None):
    if path is None:
        path = [spot]

    if spot == "end":
        yield path
    else:
        for node in map[spot]:
            if (is_small(node) and node in path):
                continue
            for result in find_path(map, node, path + [node]):
                yield result


def path_has_two_small_caves(path):
    small_caves = [spot for spot in path if is_small(spot)]
    frequency = collections.Counter(small_caves)
    m = max(dict(frequency).values())

    if m > 1:
        return True
    else:
        return False


def part2_path(map,spot,path=None):
    if path is None:
        path = [spot]

    if spot == "end":
        yield path
    else:
        for node in map[spot]:
            if node == "start":
                continue
            if is_small(node) and path_has_two_small_caves(path) and node in path:
                continue
            for result in part2_path(map, node, path + [node]):
                yield result


def make_map(segments):
    map = {}
    for segment in segments:
        (p1, p2) = segment.split("-")
        if p1 in map:
            map[p1].append(p2)
        else:
            map[p1] = [p2]
        if p2 in map:
            map[p2].append(p1)
        else:
            map[p2] = [p1]

    return map


def part1(input):
    with open(input) as f:
        segments = f.read().splitlines()

    map = make_map(segments)
    paths = find_path(map, "start")
    count = 0
    for p in paths:
        count += 1
    #        print("Path {} - {} is end".format(p, "end" in p))

    return (str(count))


def part2(input):
    with open(input) as f:
        segments = f.read().splitlines()

    map = make_map(segments)
    paths = part2_path(map, "start")
    count = 0
    for p in paths:
        count += 1
#        print("Path {}".format(p))

    return (str(count))
