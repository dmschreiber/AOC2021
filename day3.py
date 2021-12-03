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

def part2(input):
    with open(input) as f:
        numbers = f.read().splitlines()

    number_count = len(numbers)
    ox = ""

    for i in range(0,len(numbers[0])):
        bit_total = float(0)
        bit_count = float(0)

        for n in numbers:
            if n[:len(ox)] == ox :
                bit_total = bit_total + float(n[i])
                bit_count = bit_count + 1
                last = n

        if bit_count == 1 :
            ox = last
            break
        else:
            if bit_total / bit_count >= 0.5 :
                ox = ox + "1"
            else:
                ox = ox + "0"

    co = ""
    for i in range(0,len(numbers[0])):
        bit_total = float(0)
        bit_count = float(0)

        for n in numbers:
            if n[:len(co)] == co :
                bit_total = bit_total + float(n[i])
                bit_count = bit_count + 1
                last = n

        if bit_count == 1 :
            co = last
            break
        else:
            if bit_total / bit_count >= 0.5 :
                co = co + "0"
            else:
                co = co + "1"

    print("ox {}, co2 {}".format(ox, co))

    result = int(ox,2) * int(co,2)
    return str(result)