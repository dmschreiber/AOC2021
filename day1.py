def part1(input):
    with open(input) as f:
        depths = f.read().splitlines()


    count = 0
    last = 99999
    for depth in depths:
        if int(depth) > int(last):
            count = count + 1

        last = int(depth)

    return(str(count))

def part2(input):
    with open(input) as f:
        depths = f.read().splitlines()
    count = 0
    total_count = 0

    for i in range(0,len(depths)-3):
        total_count = total_count + 1
#        print("index {}, size {}".format(i, len(depths)))
        sum1 = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
        sum2 = int(depths[i+1]) + int(depths[i+2]) + int(depths[i+3])
        print("Sum: {}".format(sum1))
        if sum2 > sum1 :
            count = count + 1


    return(str(count))
