import re
import math


def add(num1,num2):
    return "[" + num1 + "," + num2 + "]"


def reduce(num):
    new_num = explode(num)
    if new_num != num:
        return new_num

    new_num = split_num(num)
    if new_num != num:
        return new_num

    return num


def magnitude(num):
    if re.match(r'^\d+$', num):
        return int(num)

    if re.match(r'\[\d+,[0-9]+\]', num):
        return 3*int(num[1]) + 2*int(num[3])

    inside_num = num[1:len(num)-1]
    count = 0
    print("Checking inside_num {}".format(inside_num))
    for i in range(len(inside_num)):
        if count == 0 and inside_num[i] == ",":
            left_part = inside_num[:i]
            right_part = inside_num[i+1:]
            return magnitude(left_part) * 3 + magnitude(right_part) * 2
        if inside_num[i] == '[':
            count += 1
        elif inside_num[i] == ']':
            count -= 1


def split_num(num):
    all_nums = re.findall(r'\d+', num)
    for i in range(len(all_nums)):
        if int(all_nums[i]) >= 10:
            new_left = math.floor(int(all_nums[i])/2)
            new_right = math.ceil(int(all_nums[i])/2)
            pos_num = num.find(all_nums[i])
            num = num[:pos_num] + "[" + str(new_left) + "," + str(new_right) + "]" + num[pos_num + len(all_nums[i]):]
            return num

    return num

def explode(num):
    left_count = 0
    for i in range(len(num)):
        if left_count == 5:
            left_part = num[:i - 1]
            right_part = num[num.find("]", i) + 1:]
            middle_part = num[i:num.find("]", i)]
            print("{}  {}  {}".format(left_part, middle_part, right_part))
            print("Middle part {}".format(middle_part))
            left_num = int(middle_part.split(",")[0])
            right_num = int(middle_part.split(",")[1])
            first_num = re.findall(r'\d+', right_part)
            if len(first_num) > 0:
                first_num = first_num[0]
            else:
                first_num = None

            last_num = re.findall(r'\d+', left_part)
            if len(last_num) > 0:
                last_num = last_num[len(last_num) - 1]
            else:
                last_num = None

            if first_num is not None:
                right_part = re.sub("[0-9]+", str(right_num + int(first_num)), right_part, 1)
            if last_num is not None:
                last_position = left_part.rfind(last_num)
                left_part = left_part[:last_position] + str(left_num + int(last_num)) + left_part[
                                                                                        last_position + len(last_num):]
            return left_part + "0" + right_part

        if num[i] == "[":
            left_count += 1
        elif num[i] == "]":
            left_count -= 1
    return num


def add_nums(num1, num2):
    total = add(num1,num2)
    last_total = ""

    while total != last_total:
        last_total = total
        total = reduce(total)

    return total

def part1(input):
    with open(input) as f:
        nums = f.read().splitlines()

    running_sum = add_nums(nums[0],nums[1])
    for i in range(2, len(nums)):
        running_sum = add_nums(running_sum, nums[i])
    print("Resulting num {}".format(running_sum))
    return(magnitude(running_sum))

def part2(input):
    with open(input) as f:
        depths = f.read().splitlines()
    count = 0



    return(str(count))
