import statistics

def calculate_fuel_part1(nums, num):
    sum = 0
    for n in nums:
        sum = sum + abs(n-num)

    return sum

def calculate_fuel_part2(nums, num):
    total = 0
    for n in nums:
        total = total + sum(range(1,abs(n-num)+1))

    return total

def part1(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    numbers = [int(n) for n in input_lines[0].split(",")]
    median = statistics.median(numbers)

    target = median

    return str(calculate_fuel_part1(numbers,int(statistics.median(numbers))))

def part2(input):
    with open(input) as f:
        input_lines = f.read().splitlines()

    numbers = [int(n) for n in input_lines[0].split(",")]

    minimum = min(numbers)
    maximum = max(numbers)

    target = int((minimum + maximum) / 2)

    while not (calculate_fuel_part2(numbers,target -1 ) > calculate_fuel_part2(numbers,target) and calculate_fuel_part2(numbers,target) < calculate_fuel_part2(numbers,target+1)):
        if calculate_fuel_part2(numbers,target -1 ) > calculate_fuel_part2(numbers,target):
            minimum = target
            target = int((minimum+maximum)/2)

        else:
            maximum = target
            target = int((minimum+maximum)/2)

    current_fuel = calculate_fuel_part2(numbers,target)

    return str(current_fuel)