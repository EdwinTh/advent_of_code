import re
with open("data02.txt") as d:
    data = d.readlines()

def checksum_line(l):
    ints = [int(nr) for nr in re.findall("\d+", l)]
    return max(ints) - min(ints)

print("Value for star 1 is " + str(sum([checksum_line(l) for l in data])))

def evenly_divisible(l):
    ints = [int(nr) for nr in re.findall("\d+", l)]
    ints.sort(reverse = True)
    for i in range(len(ints) -1):
        for j in range(i+1, len(ints)):
            if ints[i] % ints[j] == 0:
                return ints[i] // ints[j]

print("Value for star 2 is " + str(sum([evenly_divisible(l) for l in data])))