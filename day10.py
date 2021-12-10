values = {")": 3, "]": 57, "}": 1197, ">": 25137 }
part2_values = {")": 1, "]": 2, "}": 3, ">": 4 }

close_open_matching = {")": "(", "]":"[", "}":"{", ">":"<"}
open_close_matching = {"(":")", "[":"]", "{":"}", "<":">"}


def print_char(stack,c):
    indent = [" " for i in range(len(stack))]
    f = "".join(indent)
    print(f, end="")
    print("{}".format(c))

def incomplete(line):
    stack = []
    for i in range(len(line)):
        c = line[i:i + 1]
        if c in ("(", "[", "{", "<"):
            stack.append(c)
        #            print_char(stack,c)

        elif c in (")", "]", "}", ">"):
            if stack[len(stack) - 1] == close_open_matching[c]:
                #                print_char(stack, c)
                stack.pop()

            else:
                return c

    stack.reverse()
    stack = [open_close_matching[i] for i in stack]
    return "".join(stack)

def parse(line):
    stack = []
    for i in range(len(line)):
        c = line[i:i+1]
        if c in ("(", "[", "{", "<"):
            stack.append(c)
#            print_char(stack,c)

        elif c in (")", "]", "}", ">"):
            if stack[len(stack)-1] == close_open_matching[c] :
#                print_char(stack, c)
                stack.pop()

            else:
                return c

    return ""

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    frequency = {")": 0, "]": 0, "}": 0, ">": 0}
    incomplete_lines = []

    for line in input_lines:
        c = parse(line)
        if c != "":
            frequency[c] += 1

    total = sum([values[c]*frequency[c] for c in values.keys()])
    return str(total)

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    frequency = {")": 0, "]": 0, "}": 0, ">": 0}
    incomplete_lines = []

    for line in input_lines:
        c = parse(line)
        if c != "" :
            frequency[c] += 1
        else :
            if incomplete(line) != "":
                incomplete_lines.append(line)

    # print(incomplete_lines)
    scores = []
    for l in incomplete_lines :
        remainder = incomplete(l)
        score = 0
        for c in list(remainder) :
            score = score * 5 + part2_values[c]

        scores.append(score)

    scores.sort()
    middle = int(len(scores) / 2)
    return str(scores[middle])
