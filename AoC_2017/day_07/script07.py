import re
with open("data07.txt") as d:
    data = d.readlines()
data = [d.strip().split(' -> ') for d in data]
left = []
right = []
for el in data:
    left = left + re.findall('[a-z]+', el[0])
    if len(el) == 2:
        right = right + el[1].split(", ")
print("Star 1 : ")
print(set(left).difference(set(right)))
