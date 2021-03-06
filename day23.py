import copy
from itertools import chain
import time


room = {}
room["A"] = [(1, 3), (2, 3)]
room["B"] = [(1, 5), (2, 5)]
room["C"] = [(1, 7), (2, 7)]
room["D"] = [(1, 9), (2, 9)]
spots = [(0, 1), (0, 2), (0, 4), (0, 6), (0, 8), (0, 10), (0, 11)]
energy = {"A": 1, "B": 10, "C": 100, "D": 1000}


def part1(input):
    locations = load_input(input)


    start_time = time.perf_counter()
    # move(locations, "B", (1, 3), (0, 2))
    # move(locations, "D", (1, 9), (0, 10))
    # print_detail(locations)
    # available_moves = get_all_available_moves(locations)
    # available_moves.sort(key=lambda x: 0 if x[2] in room[x[0]] else calculate_power(x[1], x[2], x[0]))
    # print("order of moves {}".format(available_moves))
    # exit(0)

    min_power = None
    for p in play_game(locations):
        min_power = int(p)
        end_time = time.perf_counter()
        print (f"Powers {p} - {end_time - start_time:0.6f}s")

    return(str(min_power))

# 41653 too low
def part2(input):
    locations = load_input(input)

    room["A"] += [(3,3),(4,3)]
    room["B"] += [(3,5),(4,5)]
    room["C"] += [(3,7),(4,7)]
    room["D"] += [(3,9),(4,9)]

    for type in locations:
        for index in range(len(locations[type])):
            if locations[type][index][0] == 2:
                locations[type][index] = (locations[type][index][0]+2,locations[type][index][1])

    locations["A"] += [(2,9),(3,7)]
    locations["B"] += [(3,5),(2,7)]
    locations["C"] += [(2,5),(3,9)]
    locations["D"] += [(2,3),(3,3)]

    # print_detail(locations)
    # move(locations, "D", (1,9),(0,11))
    # move(locations, "A", (2,9),(0,1))
    # move(locations, "B", (1,7),(0,10))
    # move(locations, "B", (2,7),(0,8))
    # move(locations, "A", (3,7),(0,2))
    # move(locations, "C", (1,5),(3,7))
    # move(locations, "C", (2,5),(2,7))
    # move(locations, "B", (3,5),(0,6))
    # move(locations, "D", (4,5),(0,4))
    # move(locations, "B", (0,6), (4,5))
    # move(locations, "B", (0,8), (3,5))
    # move(locations, "B", (0,10),(2,5))
    # move(locations, "C", (3,9), (1,7))
    # move(locations, "A", (4,9), (0,10))
    # move(locations, "D", (0,4),(4,9))
    # move(locations, "B", (1,3), (1,5))
    # move(locations, "D", (2,3),(3,9))
    # move(locations, "D", (3,3),(2,9))
    # print_detail(locations)
    # exit(0)
    start_time = time.perf_counter()
    min_power = None
    for p in play_game(locations):
        min_power = int(p)
        end_time = time.perf_counter()
        print (f"Powers {p} - {end_time - start_time:0.6f}s")

    return(str(min_power))


def copy_locations(locations):
    new_locations = {}
    for type in locations.keys():
        new_locations[type] = locations[type].copy()

    return new_locations


def remove_available_spot(available, location):
    if location in available:
        available.remove(location)


def whats_where(locations, location):
    for type in locations.keys():
        for l in locations[type]:
            if l == location:
                return type

    return None


def available_spaces(locations, type, location):
    # spots plus my room minus occupied and blocked

    available = []
    if location[0] != 0: # if i'm not in the hall I can move to the hall
        available += spots
    # print("Available -1 {}".format(available))

    # update for deeper caves
    # room is available if it only contains the right type
    if len(room[type])>2:
        whats_in_the_room = [whats_where(locations,r) for r in room[type]]
        if set(whats_in_the_room) == {None, type}:
            # available += room[type]
            # if my room is empty, I can only move to the bottom
            available += [(max([r[0] for r in room[type] if whats_where(locations, r) is None]),max([r[1] for r in room[type]]))]
        # if my room is empty, I can only move to the bottom
        elif set(whats_in_the_room) == {None}:
            available = [(len(room[type]), room[type][0][1])]

    else:
        if whats_where(locations,room[type][1]) == type:
            available += [(room[type][0][0],room[type][0][1])]

        if whats_where(locations,room[type][0]) is None and whats_where(locations,room[type][1]) is None:
            available += [(room[type][1][0],room[type][1][1])]

    for i in list(chain(*locations.values())):
        remove_available_spot(available,i)

        if i[0] == 0 and i[1] < location[1]:
            for j in range(i[1]):
                for k in range(len(room[type])+1):
                    remove_available_spot(available,(k,j))

        if i[0] == 0 and i[1] > location[1]:
            for j in range(i[1],12):
                for k in range(len(room[type])+1):
                    remove_available_spot(available,(k,j))

    # update for deeper caves
    if location[0] == 2 and (1,location[1]) in list(chain(*locations.values())):
        available= []

    # print("Available 0 {}".format(available))
    if len(room[type])>2:
        if location[0] == 3 and \
                (   (1,location[1]) in list(chain(*locations.values())) or
                    (2,location[1]) in list(chain(*locations.values())) ):
            available = []
        if location[0] == 4 and \
                (   (1,location[1]) in list(chain(*locations.values())) or
                (2,location[1]) in list(chain(*locations.values())) or
                (3,location[1]) in list(chain(*locations.values())) ):
            available = []
    # print("Available 1 {}".format(available))
    if location in room[type] and \
            ( set([whats_where(locations,r) for r in room[type]]) == {None, type} or
              set([whats_where(locations, r) for r in room[type]]) == {type} ):
        available = []
    # print("Available 2 {}".format(available))

    if len(available) > 0 and max([a[0] for a in available]) > 0:
        available = [(a[0],a[1]) for a in available if a[0] > 0]

    # available.sort(key=lambda x: manhattan_distance(x,location))
    # available.sort(reverse=True)

    return available


def manhattan_distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])



def move(locations, type, location, new_location):
    if not (new_location in available_spaces(locations, type, location) and whats_where(locations,location) == type):
        print(f"Failed to move {type} from {location} to {new_location}")
        if not(new_location in available_spaces(locations, type, location)):
            print("New location not available")
        if whats_where(locations,location) != type:
            print(f"I think {whats_where(locations,location)} is there not {type}")
        print_detail(locations)

    assert(new_location in available_spaces(locations, type, location) and whats_where(locations,location) == type)

    power = calculate_power(location, new_location, type)

    for search_type in locations:
        for index in range(len(locations[search_type])):
            if locations[search_type][index] == location:
                locations[search_type][index] = new_location

    return power


def calculate_power(location, new_location, type, debug=False):
    distance = manhattan_distance(location, new_location)
    if debug:
        print(f"manhattan distance {location} to {new_location} - {distance}")

    if location[0] == new_location[0] == 1:
        distance += 2
    elif location[0] == new_location[0] == 2:
        distance += 4
    elif location[0] == new_location[0] == 3:
        distance += 6
    elif location[0] == new_location[0] == 4:
        distance += 8
    elif min(location[0], new_location[0]) == 1 and max(location[0], new_location[0]) == 2:
        distance += 2
    elif min(location[0], new_location[0]) >= 1 and max(location[0], new_location[0]) >= 1:
        distance += min(location[0], new_location[0])*2

    if debug:
        print(f"final distance {distance}")

    power = energy[type] * distance
    return power


def check_room_done(locations, type):
    for r in room[type]:
        if whats_where(locations, r) is None or whats_where(locations, r) != type:
            return False
    return True

def check_done(locations):
    for type in ["A","B","C","D"]:
        if not check_room_done(locations, type):
            return False

    return True


def power_required_next_move(locations, type, old_location, new_location):
    location_copy = copy_locations(locations)
    for l in range(len(location_copy[type])):
        if location_copy[type][l] == old_location:
            location_copy[type][l] = new_location
    return min_power_required(location_copy)


def sum_of_how_close_to_home(locations):
    total = 0
    for type in ["A","B","C","D"]:
        for location in locations[type]:
            total += abs(location[1] - room[type][0][1])

    return total


def sort_order(locations, type, old_location, new_location):

    if new_location in room[type]:
        return 0

    location_copy = copy_locations(locations)

    for l in range(len(location_copy[type])):
        if location_copy[type][l] == old_location:
            location_copy[type][l] = new_location

    if True in [set([whats_where(location_copy, r) for r in room[each_type]]) == {None} for each_type in list("ABCD")]:
        # print_detail(location_copy)
        return 1

    # if type in list("AD"):
    #     return 3
    # if type in list("BC"):
    #     return 4

    # return min_power_required(location_copy)

    # return sum_of_how_close_to_home(location_copy)

    if type=="A":
        return abs(new_location[1]-3)
    elif type=="B":
        return abs(new_location[1]-5)
    elif type=="C":
        return abs(new_location[1]-7)
    elif type=="D":
        return abs(new_location[1]-9)


    if available_spaces(location_copy, type, new_location) == []:
        return energy["D"]*(len(room[type])+1+len(spots))


    # return sum_of_how_close_to_home(location_copy)

    # return calculate_power(old_location, new_location, type)




def play_game(locations, moves = None, power = 0, type = None, location = None, new_location = None, min_power = None):
    if moves is None:
        moves = []
    move_power = 0

    # print("Moves {}".format(len(moves)))

    if type is not None:
        # if min_power == 12521:
        #     print_detail(locations)
        #     print("Moving {} from {} to {}".format(type, location, new_location))
        #     print("Current power {}".format(power))
        move_power = move(locations, type, location, new_location)

    # print_detail(locations)

    if check_done(locations):
        if min_power is None or power+move_power < min_power:
            # print("Moves {}".format(moves))
            min_power = power+move_power
            yield int(power + move_power)

    elif min_power is None or min_power > move_power + power + min_power_required(locations):
        available_moves = get_all_available_moves(locations)

        # prioritize moves into my room
        available_moves.sort(key=lambda x: sort_order(locations, x[0], x[1], x[2]))
        # print("Available moves {}".format(available_moves))
        # print_detail(locations)
        # exit(-1)
        for available_move in available_moves:
            (move_type, move_location, next_location) = available_move
            if min_power is not None and min_power <= move_power + power:
                break
            if min_power is not None and min_power <= move_power + power + power_required_next_move(locations, move_type, move_location, next_location):
                continue

            new_locations = copy_locations(locations)

            # if min_power == 13558:
            #     print("Still looking for something less power={} with min_power_required={}".format(power+move_power, power_required_next_move(new_locations, move_type, move_location, next_location)))
            #     print("Play {} from {} to {}".format(move_type, move_location, next_location))
            #     print_detail(new_locations)

            for p in play_game(new_locations, moves.copy() + ["{}: {}->{}".format(move_type,move_location,next_location)], power + move_power, move_type, move_location, next_location, min_power):
                if min_power is None or p < min_power:
                    min_power = p
                    # print("Min power {}".format(min_power))
                    yield p


#calc min power required for everyoen to get to their rooms
def min_power_required(locations, debug = False):
    power_required = 0
    how_many_outside_rooms = {}

    for type in list("ABCD"):
        how_many_outside_rooms[type] = 0

    for type in locations.keys():
        for location in locations[type]:
            if location not in room[type]:
                if debug:
                    print("location not in room - {}/{} {}; requires {} power to move to {}".format(type, how_many_outside_rooms[type], location, calculate_power(location, room[type][how_many_outside_rooms[type]], type, debug), room[type][how_many_outside_rooms[type]]))

                power_required += calculate_power(location, room[type][how_many_outside_rooms[type]], type)
                how_many_outside_rooms[type] += 1

    # if max([how_many_outside_rooms[type] for type in list("ABCD")]) > 1 and not debug:
    #     print_detail(locations)
    #     min_power_required(locations, True)
    #     exit(-1)

    return power_required


def get_all_available_moves(locations):
    available_moves = []
    for type in list("ABCD"):
        if not check_room_done(locations, type):
            for location in locations[type]:
                if location != room[type][1]:
                    available_moves += [(type, location, s) for s in available_spaces(locations, type, location)]

    return available_moves


def print_detail(locations):
    print(locations)
    for i in range(len(room["A"])+1):
        for j in range(13):
            if i>0 and j> 2 and j < 10 and j/2==int(j/2):
                print("#",end="")
            elif (i==0 and j>0 and j<12) or (i>0 and j>2 and j<10):
                if whats_where(locations, (i,j)) is None:
                    print(".", end="")
                else:
                    print(whats_where(locations, (i,j)), end="")
            else:
                print("#", end="")
        print("")

    for type in locations.keys():
        for location in locations[type]:
            available_moves = available_spaces(locations, type, location)
            available_moves.sort(key=lambda x: sort_order(locations, type, location, x))
            print("For {} at {} can move {}".format(type, location, available_moves))


def load_input(input):
    with open(input) as f:
        input_lines = f.read().splitlines()
    locations = {}
    for i in range(1, 3):
        for j in range(4):
            if input_lines[i + 1][3 + j * 2:3 + j * 2 + 1] in locations.keys():
                locations[input_lines[i + 1][3 + j * 2:3 + j * 2 + 1]] += [(i, 3 + j * 2)]
            else:
                locations[input_lines[i + 1][3 + j * 2:3 + j * 2 + 1]] = [(i, 3 + j * 2)]
    return locations


