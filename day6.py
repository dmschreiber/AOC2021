def part1(input, days):
    with open(input) as f:
        input_lines = f.read().splitlines()

    numbers = [int(n) for n in input_lines[0].split(",")]
#    print("Initial state: {}".format(numbers))
    for i in range(days):
        new_numbers = []
        spawn = numbers.count(0)
        for j in range(len(numbers)):
            if numbers[j] > 0:
                numbers[j] = numbers[j] - 1
            else:
                numbers[j] = 6

        for j in range(spawn):
            numbers.insert(len(new_numbers),8)

        #numbers = new_numbers
#        print("{}\t{}".format(i+1,len(numbers)))

    return str(len(numbers))

def part2(input,days):
    with open(input) as f:
        input_lines = f.read().splitlines()

    numbers = [int(n) for n in input_lines[0].split(",")]

    n = [numbers.count(i) for i in range(9)]
    for s in range(days):
        z=n[0]
        n[0:8]=n[1:9]
        n[6]+=z
        n[8]=z
    return str(sum(n))
    