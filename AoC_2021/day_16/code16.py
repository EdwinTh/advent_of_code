from mapping import m
data = [el for el in open('test_data.txt')][0]
packet = "".join([m[hex] for hex in data])

def process_literal(lv):
    # no_zeros = str(int(literal_value[::-1]))[::-1]
    broken_up = [lv[i*5:i*5+5] for i in range(len(lv) / 5)]
    nr_to_process = ""
    zero_cnt = 0
    for bu in broken_up:
        if zero_cnt > 1:
            break
        nr_to_process += bu[1:]
        if bu[0] == '0':
            zero_cnt += 1
        broken_up = broken_up[1:]
    return int(nr_to_process, 2), "".join(broken_up)


def process_packet(packet, processed = []):
    version = int(packet[:3], 2)
    print(packet[3:6])
    ID = int(packet[3:6], 2)
    processed.append([version, ID])
    if ID == 4:
        value, packet = process_literal(packet[6:])
        processed[-1].append(value)
        while '1' in packet:
            version = int(packet[:3], 2)
            ID = int(packet[3:6], 2)
            value, packet = process_literal(packet)
            processed.append([version, ID, value])
    else:
        if packet[6] == '0':
            l = int(packet[7:22], 2)    
            processed[-1].append(process_packet(packet[22:22+l]))
        else:
            l = int(packet[7:18], 2)
            process_packet

    return processed


# print(sum([el[1] for el in process_packet(packet)]))
print(process_packet(packet))

            
