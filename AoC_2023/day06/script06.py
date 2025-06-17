import re
import numpy as np
with open('data06.txt') as d:
    data = [el.strip() for el in d.readlines()]

times = [int(d) for d in re.findall("\d+", data[0])]
distances = [int(d) for d in re.findall("\d+", data[1])]

def get_distance(seconds, time):
    return (time - seconds) * seconds

def get_all_distances(time):
    return [get_distance(t, time) for t in range(1, time+1)]

def get_nr_options(time, distance):
    all_dists = get_all_distances(time)
    return len([d for d in all_dists if d > distance])

options = [get_nr_options(times[i],distances[i]) for i in range(len(times))]
print("Star 1:",  str(np.prod(options)))

def collapse(l):
    nr = ''
    for el in l:
        nr += str(el)
    return int(nr)

time = collapse(times)
dist = collapse(distances)

first = 1
last = time

while True:
    dist_t = get_distance(first, time)
    if dist_t > dist: break
    first += 1

while True:
    dist_t = get_distance(last, time)
    if dist_t > dist: break
    last -= 1
print("Star 2:", str(last - first + 1))

