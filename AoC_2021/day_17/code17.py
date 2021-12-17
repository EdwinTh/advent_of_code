import re
import itertools
data  = [el.strip() for el in open('data.txt')][0]
# star 1
coords = re.findall('-?\d+', data)
coords = [int(c) for c in coords]
c = {'xmin':min(coords[:2]), 'xmax':max(coords[:2]), 'ymin':min(coords[2:]), 'ymax':max(coords[2:])}

def get_trajectory(x, y):
    t = [(x, y)]
    while t[-1][0] < c['xmax'] and t[-1][1] > c['ymin']:
        y -= 1
        x = x - 1 if x > 0 else 0
        t = t + [(t[-1][0] + x, t[-1][1] + y)]
    return t

def hit_target(traj):
    def hit_it(traj_el):
        return traj_el[0] >= c['xmin'] and traj_el[0] <= c['xmax'] and \
               traj_el[1] >= c['ymin'] and traj_el[1] <= c['ymax']
    return any([hit_it(traj_el) for traj_el in traj])

def max_y(traj):
    return max([t[1] for t in traj])

def evaluate_comb(comb):
    x = comb[0]; y = comb[1]
    traj = get_trajectory(x, y)
    hit = hit_target(traj)
    return max_y(traj) if hit else None

all_combs = list(itertools.product(range(1, 100), range(0, 100)))

print(max([evaluate_comb(comb) for comb in all_combs]))

# star 2
def evaluate_comb2(comb):
    x = comb[0]; y = comb[1]
    traj = get_trajectory(x, y)
    hit=  hit_target(traj)
    return hit

all_combs = list(itertools.product(range(1, c['xmax'] + 1), range(c['ymin'], 500)))
print(sum([evaluate_comb2(comb) for comb in all_combs]))