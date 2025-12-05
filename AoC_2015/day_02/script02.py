from math import prod
with open('data02.txt') as d:
    data = [el.strip().split('x') for el in d.readlines()]
    data = [[int(e) for e in element] for element in data]

sides = [[e[0]*e[1], e[0]*e[2], e[1]*e[2]] for e in data]
paper = [min(e) + sum(e) * 2 for e in sides]

print("Star 1:", sum(paper))

data_sorted = [sorted(d) for d in data]
ribbon = [2*d[0] + 2*d[1] + prod(d) for d in data_sorted]

print("Star 2:", sum(ribbon))
