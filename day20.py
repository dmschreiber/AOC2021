def part1(input):
    return run_sumulation(input, 2)


def part2(input):
    return run_sumulation(input, 2)



def run_sumulation(input, iterations):
    decoder, image = read_input(input)

    print_image(image)

    for step in range(iterations):
        new_image = {}
        min_row = min([item[0] for item in image.keys()])
        max_row = max([item[0] for item in image.keys()])
        min_col = min([item[1] for item in image.keys()])
        max_col = max([item[1] for item in image.keys()])

        # for row in range(-1*step-1,original_max_row+step+2):
        #     for col in range(-1*step-1,original_max_col+step+2):
        #         new_image[(row,col)] = process(image,decoder,row,col,step)

        for row in range(min_row-5,max_row+5):
            for col in range(min_row-5,max_col+5):
                new_image[(row,col)] = process(image,decoder,row,col,step)


        image = new_image
        print_image(image)

    # return the magic number
    old_count = sum([i for i in image.values()])
    print("old count {}".format(old_count))
    count = 0
    for row in range(-1*iterations,original_max_row+iterations+1):
        for col in range(-1*iterations,original_max_col+iterations+1):
            if (row,col) in image.keys() and image[(row, col)] > 0:
                count += 1

    return(count)


def print_image(image):
    # print
    print("row min/max {} {}".format(min([item[0] for item in image.keys()]), max([item[0] for item in image.keys()])))
    print("col min/max {} {}".format(min([item[1] for item in image.keys()]), max([item[1] for item in image.keys()])))

    min_row = min([item[0] for item in image.keys()])
    max_row = max([item[0] for item in image.keys()])
    min_col = min([item[1] for item in image.keys()])
    max_col = max([item[1] for item in image.keys()])

    for row in range(min_row - 1, max_row + 2):
        print("{:3}".format(row), end="")
        for col in range(min_col - 1, max_col + 2):
            if (row,col) in image.keys() and image[(row, col)] > 0:
                print("#", end="")
            else:
                print(".", end="")
        print()


original_max_row = 0
original_max_col = 0
decoder = []


def read_input(input):
    global original_max_row
    global original_max_col
    global decoder


    with open(input) as f:
        input_lines = f.read().splitlines()
    decoder = input_lines[0]

    print("Decoder = {}".format(decoder))
    decoder = [1 if item == "#" else 0 for item in list(decoder)]
    print("Decoder = {}".format(decoder))
    image = {}
    for row in range(0, len(input_lines) - 2):
        for col in range(len(input_lines[row + 2])):
            image[(row, col)] = [1 if item == "#" else 0 for item in list(input_lines[row + 2])][col]

    original_max_row = max([item[0] for item in image.keys()])
    original_max_col = max([item[1] for item in image.keys()])

    return decoder, image


def process(image,decoder,my_row,my_col,step):
    number = which_spot_in_decoder(image, my_col, my_row, step)
    result = decoder[number]

    return(result)


def get_pixel(image, my_col, my_row, step):
    # if my_row < -1*step-1 or my_row > original_max_row+step+2:
    #     if int(step/2) == step/2:
    #         return 0
    #     else:
    #         return decoder[0]
    #
    # if my_col < -1*step-1 or my_col > original_max_col+step+2:
    #     if int(step/2) == step/2:
    #         return 0
    #     else:
    #         return decoder[0]


    if (my_row,my_col) in image.keys():
        return image[(my_row, my_col)]
    else:
        return 0

def which_spot_in_decoder(image, my_col, my_row, step):
    number = ""
    for row in range(my_row - 1, my_row + 2):
        for col in range(my_col - 1, my_col + 2):
            number += str(get_pixel(image, col, row, step))

    number = int(number, 2)

    return number


