import functools

def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

class BasePacket:
    def __init__(self, version, type):
        self.version = version
        self.type = type

class LiteralPacket(BasePacket):
    def __init__(self, version, type, value):
        super().__init__(version, type)
        self.value = value

    def eval(self):
        return self.value

    def sum_versions(self):
        return self.version

class OperatorPacket(BasePacket):
    def __init__(self, version, type, child_packets):
        super().__init__(version, type)
        self.child_packets = child_packets

    def sum_versions(self):
        return self.version + sum(map(lambda x: x.sum_versions(), self.child_packets))

    def eval(self):
        if self.type == 0:
            return sum(map(lambda x: x.eval(), self.child_packets))
        elif self.type == 1:
            product = 1
            for p in self.child_packets:
                product *= p.eval()
            return product

        elif self.type == 2:
            return min(map(lambda x: x.eval(), self.child_packets))
        elif self.type == 3:
            return max(map(lambda x: x.eval(), self.child_packets))
        elif self.type == 5:
            return 1 if self.child_packets[0].eval() > self.child_packets[1].eval() else 0
        elif self.type == 6:
            return 1 if self.child_packets[0].eval() < self.child_packets[1].eval() else 0
        elif self.type == 7:
            return 1 if self.child_packets[0].eval() == self.child_packets[1].eval() else 0
        else:
            raise Exception('Unknown operator type: {}'.format(self.type))
def parse_packet(packet, packet_limit = None):

    offset = 0
    sum_version = 0
    packet_list = []

    # offset < len(packet):
    count = 0
    while packet[offset:] != "" and int(packet[offset:],2) > 0 and (packet_limit is None or count < packet_limit):
        version = int(packet[offset:offset+3],2)
#        print("Found packet version {} ({} offset {})".format(version,packet[offset:],offset))
        sum_version += version
        offset = offset + 3

        count += 1

        packet_type = int(packet[offset:offset+3],2)
        offset = offset + 3

        if packet_type == 4:
#            print("Literal packet")
            last_piece = False
            literal_bits = ""
            while not last_piece:
                first_bit = packet[offset:offset+1]
                literal_bits += packet[offset+1:offset+5]
                last_piece = (first_bit == "0")
                offset += 5
            packet_list.append(LiteralPacket(version, packet_type, int(literal_bits,2)))

        else:
#            print("Operator packet")
            length_type_id = packet[offset:offset+1]
            offset += 1

            if length_type_id == "0":
                bit_length = int(packet[offset:offset+15],2)
                offset += 15
                sub_packets = packet[offset:offset+bit_length]

                child_sum, child_offset, child_packet_list = parse_packet(sub_packets)
                sum_version += child_sum
                offset += bit_length
                packet_list.append(OperatorPacket(version, packet_type, child_packet_list))
            else:
                num_subpackets = int(packet[offset:offset+11],2)
                offset += 11
                child_sum, child_offset, child_packet_list = parse_packet(packet[offset:], num_subpackets)
                sum_version += child_sum
                offset += child_offset
                packet_list.append(OperatorPacket(version, packet_type, child_packet_list))

    return sum_version, offset, packet_list

def part1(input):
    with open(input) as f:
        hex_lines = f.read().splitlines()

    print("Begin Part 1")
    sum_version, offset, p = parse_packet(hex_to_bin(hex_lines[0]))

    return(str(p[0].sum_versions()))

def part2(input):
    with open(input) as f:
        hex_lines = f.read().splitlines()

    print("Begin Part 2")
    sum_version, offset, p = parse_packet(hex_to_bin(hex_lines[0]))

    return(str(p[0].eval()))

