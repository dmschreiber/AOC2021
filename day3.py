def part1(input):
    with open(input) as f:
        numbers = f.read().splitlines()

    number_count = len(numbers)
    gamma = ""
    epsilon = ""

    for i in range(0,len(numbers[0])):
        bit_total = float(0)

        for n in numbers:
            bit_total = bit_total + float(n[i])

        if bit_total / number_count > 0.5 :
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"

    print("gamma {}, epison {}".format(gamma, epsilon))

    result = int(gamma,2) * int(epsilon,2)
    return str(result)