import re
from collections import Counter

with open('data01.txt') as d:
    data = [el.strip() for el in d.readlines()]

digits = [re.findall("\d+", p) for p in data]
first = [int(d[0]) for d in digits]
second = [int(d[1]) for d in digits]
first.sort()
second.sort()
dif_scores = [abs(f - s) for f,s in zip(first, second)]
print("Star 1:", sum(dif_scores))

second_counted = Counter(second)
sim_score = 0
for f in first:
    sim_score += second_counted[f] * f
print("Star 1:", sim_score)