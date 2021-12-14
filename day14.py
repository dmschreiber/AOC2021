import collections
import time

def create_pairs(polymer):
    frequency = {}
    end = polymer[len(polymer)-1:]

    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        if pair in frequency.keys():
            frequency[pair] += 1
        else:
            frequency[pair] = 1

    return (frequency, end)


def expand_v2(map, frequency, end):

    new_frequency = {}
    for key in frequency.keys():
        if key in map.keys():
            left_segment = key[0:1] + map[key]
            right_segment = map[key] + key[1:2]
            if left_segment in new_frequency.keys():
                new_frequency[left_segment] += frequency[key]
            else:
                new_frequency[left_segment] = frequency[key]

            if right_segment in new_frequency.keys():
                new_frequency[right_segment] += frequency[key]
            else:
                new_frequency[right_segment] = frequency[key]

    print(f"{len(frequency)} pairs")

    letter_frquency = {}
    for key in new_frequency.keys():
        letter = key[0:1]
        if letter in letter_frquency.keys():
            letter_frquency[letter] += new_frequency[key]
        else:
            letter_frquency[letter] = new_frequency[key]

    if end in letter_frquency.keys():
        letter_frquency[end] += 1
    else:
        letter_frquency[end] = 1

    score = max(letter_frquency.values()) - min(letter_frquency.values())
    print(f"{len(letter_frquency)} letters score {score}")

    return(new_frequency, end, score)


def expand(map, polymer):
    start_time = time.perf_counter()

    new_polymer = ""
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        if pair in map.keys() :
            new_polymer = new_polymer + polymer[i:i+1] + map[pair]
        else:
            new_polymer = new_polymer + polymer[i:i+1]
    new_polymer = new_polymer + polymer[len(polymer)-1:len(polymer)]

    end_time = time.perf_counter()
    # print(f"Expansion of polymer size {len(polymer)} execution Time : {end_time - start_time:0.6f}")

    return new_polymer


def score_polymer(polymer):
    items = list(polymer)
    most_frequent = max(set(items), key=items.count)
    least_frequent = min(set(items), key=items.count)
    print("Most frequent: {}, Least: {}".format(most_frequent,least_frequent))
    score = sum([1 for i in items if i == most_frequent])-sum([1 for i in items if i == least_frequent])

    return(score)

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = {}
    template = input_lines[0]
    for j in range(2,len(input_lines)):
        map[input_lines[j].split(" -> ")[0]] = input_lines[j].split(" -> ")[1]

    polymer = template
    for i in range(10):
        polymer = expand(map,polymer)
        # print("after step {}: {}".format(i+1,polymer))

    count = score_polymer(polymer)

    return(str(count))

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    map = {}
    template = input_lines[0]
    for j in range(2,len(input_lines)):
        map[input_lines[j].split(" -> ")[0]] = input_lines[j].split(" -> ")[1]

    polymer = template
    score = 0
    (frequency, end) = create_pairs(polymer)
    for i in range(40):
        (frequency, end, score) = expand_v2(map, frequency, end)



    return(str(score))