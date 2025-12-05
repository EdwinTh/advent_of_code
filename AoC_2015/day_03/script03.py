with open('data03.txt') as d:
    data = [el.strip() for el in d.readlines()][0]

def deliver(input_list):
    loc = [0,0]
    locations_visited = [str(loc[0]) + '-' + str(loc[1])]
    for d in input_list:
        if d == "^":
            loc[0] += 1
        elif d == "v":
            loc[0] -= 1
        elif d == ">":
            loc[1] += 1
        else:
            loc[1] -= 1
        locations_visited.append(str(loc[0]) + '-' + str(loc[1]))
    return set(locations_visited)

print("Star 1:", len(deliver(data)))

santa = [d for nr,d in enumerate(data) if nr in range(0, len(data), 2)]
robo = [d for nr,d in enumerate(data) if nr in range(1, len(data), 2)]

print("Star 2:", len(deliver(santa).union(deliver(robo))))

