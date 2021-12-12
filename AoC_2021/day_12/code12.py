from collections import Counter
data = [el.strip().split('-') for el in open('data12.txt')]

def append_el_list(el1, el2, d):
    el_list = gates.get(el1, [])
    if el2 != 'start' and el1 != 'end':
        el_list.append(el2)
    d[el1] = el_list
    return d

def add_gates(el, gates):
    gates = append_el_list(el[0], el[1], gates)
    gates = append_el_list(el[1], el[0], gates)
    return gates

gates = {}
for el in data:
    gates = add_gates(el, gates)

paths = [['start', el] for el in gates['start']]

def expand_path(path, g):
    return [path + [el] for el in g[path[-1]]]

def has_double_lowers(path):
    cntr = Counter(path)
    is_lower_key = [key.islower() for key in cntr.keys()]
    is_visited_twice = [val > 1 for val in cntr.values()]
    return any([isl and ivt for isl, ivt in zip(is_lower_key, is_visited_twice)])

def take_next_step(paths, g, lower_func):
    new_paths = [expand_path(path, g) for path in paths]
    new_paths_flat = [path for paths in new_paths for path in paths]
    no_double_lower = [path for path in new_paths_flat if not lower_func(path)]
    finished_paths = [path for path in no_double_lower if path[-1] == 'end']
    paths = [path for path in no_double_lower if path[-1] != 'end']
    return finished_paths, paths

finished_paths = []
while len(paths) > 1:
    new_finished_paths, paths = take_next_step(paths, gates, has_double_lowers)
    finished_paths = finished_paths + new_finished_paths

print(len(finished_paths))

# star 2
def breaks_star2_rules(path):
    cntr = Counter(path)
    cntr_vals = [cntr[k] for k in cntr.keys() if k.islower() and k not in ['start', 'end']]
    if len(cntr_vals) == 0:
        return False
    return max(cntr_vals) > 2 or sum([cv > 1 for cv in cntr_vals]) > 1

paths = [['start', el] for el in gates['start']]
finished_paths = []
while len(paths) > 1:
    new_finished_paths, paths = take_next_step(paths, gates, breaks_star2_rules)
    finished_paths = finished_paths + new_finished_paths
    
print(len(finished_paths))
