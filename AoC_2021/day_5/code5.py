# star 1
import collections
with open('data5.txt') as f:
    data = f.readlines()
data = [d.strip().split(' -> ') for d in data]

def parse_element(el):
    fr = el[0].split(',')
    to = el[1].split(',')
    return {'x':[fr[0], to[0]], 'y':[fr[1], to[1]]}
    
def is_hor_vert(ft):
    if (ft['x'][0] == ft['x'][1]) or (ft['y'][0] == ft['y'][1]):
        return True
    return False

def produce_ranges(from_to):
    x = [int(x) for x in from_to['x']]
    y = [int(y) for y in from_to['y']]
    x_range = [int(i) for i in range(x[0], x[1]+1)]
    y_range = [int(i) for i in range(y[0], y[1]+1)]
    if x[0] > x[1]:
        x_range = [int(i) for i in range(x[0], x[1]-1, -1)]
    if y[0] > y[1]:
        y_range = [int(i) for i in range(y[0], y[1]-1, -1)]
    if len(x_range) == 1:
        x_range = [str(x[0])] * len(y_range)
    if len(y_range) == 1:
        y_range = [str(y[0])] * len(x_range)
    return [str(x) + '-' + str(y) for x,y in zip(x_range, y_range)]

parsed   = [parse_element(el) for el in data]
hor_vert = [p for p in parsed if is_hor_vert(p)]
ranges   = [produce_ranges(hv) for hv in hor_vert]
ranges_flat = [r for rng in ranges for r in rng]
print(len([el for el in collections.Counter(ranges_flat).values() if el > 1]))

# star 2
ranges   = [produce_ranges(psd) for psd in parsed]
ranges_flat = [r for rng in ranges for r in rng]
print(len([el for el in collections.Counter(ranges_flat).values() if el > 1]))
