import re
with open('data03.txt') as d:
    data = [el.strip() for el in d.readlines()]

chars = ""
for d in data:
    chars += d

extracted = re.findall('mul\(\d+,\d+\)', chars)
def multiply_digits(extract):
    ints = re.findall('\d+', extract)
    return int(ints[0]) * int(ints[1])

print("Star 1:", sum([multiply_digits(e) for e in extracted]))

active = ''
collect = True
for i in range(len(chars)):
    if collect:
        active += chars[i]
        if chars[i:i+7] == "don't()":
            collect = False
    else:
        if chars[i:i+4] == "do()":
            collect = True
extracted2 = re.findall('mul\(\d+,\d+\)', active)
print("Star 2:", sum([multiply_digits(e) for e in extracted2]))