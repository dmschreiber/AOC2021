def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    inputs = [line.split("|")[0].split() for line in input_lines]
    outputs = [line.split("|")[1].split() for line in input_lines]

    count = 0
    for o in outputs :
        lengths = [len(i) for i in o]
        for i in lengths :
            if i in (2,4,3,7) :
                count += 1

    return str(count)

def create_map(digits):
    map = {}
    reverse_map = {}

    for digit in digits:
        # 1,2,3,4,5,6,7,8
        sorted_digit = "".join(sorted(digit))
        # print("{} - {}".format(digit, sorted_digit))
        if len(sorted_digit) == 2:
            map[sorted_digit] = "1"
            reverse_map["1"] = sorted_digit

        if len(sorted_digit) == 3:
            map[sorted_digit] = "7"
            reverse_map["7"] = sorted_digit

        if len(sorted_digit) == 4:
            map[sorted_digit] = "4"
            reverse_map["4"] = sorted_digit

        if len(sorted_digit) == 7:
            map[sorted_digit] = "8"
            reverse_map["8"] = sorted_digit

    abdeg = [l for l in reverse_map["8"] if not(l in reverse_map["1"])]
    bd = [l for l in reverse_map["4"] if not(l in reverse_map["1"])]
    a = [l for l in reverse_map["7"] if not(l in reverse_map["1"])]

    # 6 is length six and without the digits of 1
    for digit in digits:
        sorted_digit = "".join(sorted(digit))
        if len ([l for l in reverse_map["1"] if not (l in sorted_digit)]) > 0 :
            if len(digit) == 6:
                map[sorted_digit] = "6"
                reverse_map["6"] = sorted_digit

    c = [l for l in reverse_map["8"] if not(l in reverse_map["6"])][0]

    # 2 and 5
    for digit in digits:
        sorted_digit = "".join(sorted(digit))
        if not(sorted_digit in map.keys()) :
            if len([l for l in reverse_map["1"] if not (l in sorted_digit)]) > 0:
                if len(digit) == 5 and c in digit:
                    map[sorted_digit] = "2"
                    reverse_map["2"] = sorted_digit
                else :
                    map[sorted_digit] = "5"
                    reverse_map["5"] = sorted_digit

    # 3
    for digit in digits:
        sorted_digit = "".join(sorted(digit))
        if not(sorted_digit in map.keys()) :
            if len(digit) == 5:
                map[sorted_digit] = "3"
                reverse_map["3"] = sorted_digit

    e = [l for l in reverse_map["2"] if not (l in reverse_map["3"])][0]
    f = [l for l in reverse_map["3"] if not (l in reverse_map["2"])][0]

    # 9 is eight without segment e
    nine = "".join([l for l in reverse_map["8"] if l != e])
    map[nine] = "9"
    reverse_map["9"] = nine

    # only zero is left
    for digit in digits:
        sorted_digit = "".join(sorted(digit))
        if not(sorted_digit in map.keys()) :
            if len(digit) == 6 and e in digit:
                map[sorted_digit] = "0"
                reverse_map["0"] = sorted_digit

    # for k in map.keys() :
    #    print("- {}: {}".format(k, map[k]))


    return map

def part2(input):

    with open(input) as f:
        input_lines = f.read().splitlines()

    inputs = [ line.split("|")[0].split() for line in input_lines]
    outputs = [ line.split("|")[1].split() for line in input_lines]

    total = 0
    for i in range(len(inputs)) :
        map = create_map(inputs[i])
        n = ""
        for j in range(len(outputs[i])) :
            sorted_output = "".join(sorted(outputs[i][j]))
            n = n+ map[sorted_output]

        total = total + int(n)

    return str(total)