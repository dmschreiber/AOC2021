

def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

def parse_packet(packet, packet_limit = None):

    offset = 0
    sum_version = 0

    # offset < len(packet):
    count = 0
    while packet[offset:] != "" and int(packet[offset:],2) > 0 and (packet_limit is None or count < packet_limit):
        version = int(packet[offset:offset+3],2)
        print("Found packet version {} ({} offset {})".format(version,packet[offset:],offset))
        sum_version += version
        offset = offset + 3

        count += 1

        packet_type = int(packet[offset:offset+3],2)
        offset = offset + 3

        if packet_type == 4:
            print("Literal packet")
            last_piece = False
            literal_bits = ""
            while not last_piece:
                first_bit = packet[offset:offset+1]
                literal_bits += packet[offset+1:offset+5]
                print("found literal piece {} first bit {} from {} to {}".format(packet[offset:offset+5], first_bit,offset,offset+1))
                last_piece = (first_bit == "0")
                offset += 5
        else:
            print("Operator packet")
            length_type_id = packet[offset:offset+1]
            offset += 1

            if length_type_id == "0":
                bit_length = int(packet[offset:offset+15],2)
                offset += 15
                sub_packets = packet[offset:offset+bit_length]
                print("current sum of version is {}".format(sum_version))
                child_sum, child_offset = parse_packet(sub_packets)
                sum_version += child_sum
                offset += bit_length

            else:
                num_subpackets = int(packet[offset:offset+11],2)
                offset += 11
                child_sum, child_offset = parse_packet(packet[offset:], num_subpackets)
                sum_version += child_sum
                offset += child_offset

    return sum_version, offset

def part1(input):
    with open(input) as f:
        hex_lines = f.read().splitlines()

    print("Begin Part 1")
    sum_version, offset = parse_packet(hex_to_bin(hex_lines[0]))

    return(str(sum_version))

def part2(input):
    with open(input) as f:
        depths = f.read().splitlines()
    count = 0



    return(str(count))
