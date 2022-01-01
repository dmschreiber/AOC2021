import re


def is_number(s):
    pattern = re.compile("-?\d+")
    m = pattern.match(s)

    if m:
        return True
    else:
        return False


def pad_string(s, length, pad_char):
    return  s + (pad_char * (length - len(s)))


def part1(input):
    program = load_program(input)
    model_number = 94399898949959 # RIGHT ANSSWER
    #              12345678901234
    #              999XX9XX9X99XX
    model_number = 11176161111111
    not_found = True
    options = []

    # first 999XX9XX9X99XX
    for i in range(999,111,-1):
        option = str(i)
        model_number = pad_string(option[0:4],14,"9")

        # model_number = option[0:4] + "99" + option[4:5] + "99" + option[5:6] + "9" + option[6:] + "99"

        if "0" not in str(model_number):
            # print("trying {}".format(model_number))
            registers, xvalues = run_program(model_number, program)
            if registers["z"] == 0:
                not_found = False
                print("Found {}".format(model_number))
            if 0 < xvalues[3] < 10 and \
                    0 < xvalues[4] < 10:
                options.append(option[0:3]+str(xvalues[3])+str(xvalues[4]))

    new_options = []
    for o in options:
        for i in range(9,0,-1):
            option = o + str(i)
            model_number = pad_string(option,14,"9")
            # print("trying {}".format(model_number))
            registers, xvalues = run_program(model_number, program)
            # print(xvalues)
            if registers["z"] == 0:
                not_found = False
                print("Found valid {}".format(model_number))
            if 0 < xvalues[6] < 10 and \
                    0 < xvalues[7] < 10:
                new_options.append(option+str(xvalues[6])+str(xvalues[7]))

    # print(options)
    print(new_options)
    assert("94399898"in new_options)
    options = new_options
    new_options = []

    for o in options:
        for i in range(9,0,-1):
            option = o + str(i)
            if len(option) > 9:
                print("options too big")
                exit(-1)

            model_number = pad_string(option,14,"9")
            registers, xvalues = run_program(model_number, program)
            # print(xvalues)
            if registers["z"] == 0:
                not_found = False
                print("Found valid {}".format(model_number))
            if 0 < xvalues[9] < 10:
                new_options.append(option+str(xvalues[9]))

    #check status
    print(new_options)
    right_answer = "9439989894"
    assert(len(right_answer)==len(new_options[0]))
    assert(right_answer in new_options)


    options = new_options
    new_options = []

    found = False
    for o in options:
        if found:
            break

        for i in range(99,11,-1):
            if found:
                break
            option = o + str(i)
            if len(option) > 12:
                print("options too big {}".format(option))
                exit(-1)

            model_number = pad_string(option,14,"9")

            registers, xvalues = run_program(model_number, program)

            if registers["z"] == 0:
                print("Found valid {}".format(model_number))
                found = True

            if 0 < xvalues[12] < 10:
                new_option = option+str(xvalues[12])
                for j in range(9,0,-1):
                    model_number = pad_string(new_option, 14, str(j))
                    registers, xvalues = run_program(model_number, program)

                    if registers["z"] == 0:
                        print("Found valid {}".format(model_number))
                        found = True

    return(model_number)


def run_program(number, program):
    registers = {"w": 0, "x": 0, "y": 0, "z": 0}
    input = number  # "13579246899999"
    input_index = 0
    x_values = []
    if len(number) < 14:
        print("input too short {}".format(number))
        return

    for i in range(len(program)):
        (operator, variable, value) = program[i]
        assert (variable in registers)
        assert (operator in ["inp", "add", "mul", "mod", "div", "eql"])

        if int(i % 18  ) == 6:
            x_values.append(registers["x"])

        # if input_index == 4:
        #     print("{} {} {} - x={},y={},z={}".format(operator, variable, value, registers["x"],registers["y"],registers["z"]))

        if operator == "inp":
            registers[variable] = int(list(input)[input_index])
            # print("input_index: {} input: {} w={}; ".format(input_index+1, input[input_index], registers["w"]), end="")
            input_index += 1

        elif operator == "add":
            if is_number(value):
                registers[variable] += int(value)
            else:
                registers[variable] += registers[value]
        elif operator == "mul":
            if is_number(value):
                registers[variable] *= int(value)
            else:
                registers[variable] *= registers[value]

        elif operator == "div":
            if is_number(value):
                registers[variable] = int(registers[variable] / int(value))
            else:
                registers[variable] = int(registers[variable] / registers[value])
        elif operator == "mod":
            if is_number(value):
                registers[variable] = int(registers[variable] % int(value))
            else:
                registers[variable] = int(registers[variable] % registers[value])
        elif operator == "eql":
            if is_number(value):
                if registers[variable] == int(value):
                    registers[variable] = 1
                else:
                    registers[variable] = 0
            else:
                if registers[variable] == registers[value]:
                    registers[variable] = 1
                else:
                    registers[variable] = 0

    # print("End State x={},y={},z={}".format(registers["x"], registers["y"], registers["z"]))

    return registers, x_values


def load_program(input):
    with open(input) as f:
        instructions = f.read().splitlines()
    program = []
    for i in instructions:
        if i.startswith("inp"):
            (operator, variable) = i.split()
            value = None
        else:
            (operator, variable, value) = i.split()
        program.append((operator, variable, value))
    return program


def part2(input):
    program = load_program(input)
    #              12345678901234
    #              999XX9XX9X99XX
    model_number = 11176161111111

    options = []

    # first 999XX9XX9X99XX
    for i in range(111,1000):
        option = str(i)
        model_number = pad_string(option[0:4],14,"1")

        if "0" not in str(model_number):
            # print("trying {}".format(model_number))
            registers, xvalues = run_program(model_number, program)
            if registers["z"] == 0:
                not_found = False
                print("Found {}".format(model_number))
            if 0 < xvalues[3] < 10 and \
                    0 < xvalues[4] < 10:
                options.append(option[0:3]+str(xvalues[3])+str(xvalues[4]))

    assert("11176" in options)

    new_options = []
    for o in options:
        for i in range(1,10):
            option = o + str(i)
            model_number = pad_string(option,14,"2")
            # print("trying {}".format(model_number))
            registers, xvalues = run_program(model_number, program)
            # print(xvalues)
            if registers["z"] == 0:
                not_found = False
                print("Found valid {}".format(model_number))
            if 0 < xvalues[6] < 10 and \
                    0 < xvalues[7] < 10:
                new_options.append(option+str(xvalues[6])+str(xvalues[7]))

    # print(options)
    print(new_options)
    options = new_options
    new_options = []

    for o in options:
        for i in range(1,10):
            option = o + str(i)
            if len(option) > 9:
                print("options too big")
                exit(-1)

            model_number = pad_string(option,14,"1")
            registers, xvalues = run_program(model_number, program)
            # print(xvalues)
            if registers["z"] == 0:
                not_found = False
                print("Found valid {}".format(model_number))
            if 0 < xvalues[9] < 10:
                new_options.append(option+str(xvalues[9]))

    #check status
    print(new_options)


    options = new_options
    new_options = []
    found = False

    for o in options:
        if found:
            break

        for i in range(11,100):
            if found:
                break

            option = o + str(i)
            if len(option) > 12:
                print("options too big {}".format(option))
                exit(-1)

            model_number = pad_string(option,14,"1")

            registers, xvalues = run_program(model_number, program)

            if registers["z"] == 0:
                found = True
                print("Found valid {}".format(model_number))

            elif 0 < xvalues[12] < 10:
                new_option = option+str(xvalues[12])
                for j in range(1,10):
                    model_number = pad_string(new_option, 14, str(j))
                    registers, xvalues = run_program(model_number, program)

                    if registers["z"] == 0:
                        print("Found valid {}".format(model_number))
                        found = True


    return(model_number)