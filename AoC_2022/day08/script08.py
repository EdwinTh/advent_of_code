import numpy as np
def line_to_ints(line):
    return [int(l) for l in line]
with open('data08.txt') as f:
    data = np.array([line_to_ints(line.strip()) for line in f])

def is_visible(d, x, y):
    v = d[x,y]
    return np.all(d[:x,y] < v) or np.all(d[x,:y] < v) or np.all(d[x+1:,y] < v) or np.all(d[x,y+1:] < v)

xs = range(1, data.shape[0] - 1)
ys = range(1, data.shape[1] - 1)

visible = 2 * data.shape[0] + 2 * data.shape[1] - 4
for x in xs:
    for y in ys:
        visible += is_visible(data, x, y)

print("Star 1 =", visible)

def get_score(bool_vec):
    return len(bool_vec) if np.all(bool_vec) else np.argmin(bool_vec) + 1

def get_scenic_score(d, x, y):
    v = d[x,y]
    left = get_score((d[:x,y] < v)[::-1])
    up = get_score((d[x,:y] < v)[::-1])
    right = get_score(d[x+1:,y] < v)
    down = get_score(d[x,y+1:] < v)
    return left * right * up * down

scenic = 0
for x in xs:
    for y in ys:
        scenic = max(scenic, get_scenic_score(data, x, y))
print("Star 2 =", scenic)