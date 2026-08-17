from collections import Counter
with open('data09_test.txt') as d:
    data = [el.strip().split(',') for el in d.readlines()]
    data = [[int(el) for el in d] for d in data]

def get_size(t1, t2):
    a1 = abs(t1[0] - t2[0]) + 1
    a2 = abs(t1[1] - t2[1]) + 1
    return a1 * a2

max_size = 0
for i in range(len(data)):
    for j in range(len(data)):
        if j <= i:
            continue
        max_size = max([max_size, get_size(data[i], data[j])])

print("Star 1:", max_size)

def expand_corners_to_full_edge(c1, c2):
    if c1[0] == c2[0]:
        c_range = range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1)
        return [[c1[0], c] for c in c_range]
    elif c1[1] == c2[1]:
        r_range = range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1)
        return [[r, c1[1]] for r in r_range]
    else:
        print("Both columns and rows are different, cannot expand")

outline = []

for i in range(len(data)):
    i_next = i + 1 if i < (len(data) - 1) else 0
    outline += expand_corners_to_full_edge(data[i], data[i_next])

rows = {}
cols = {}
for o in outline:
    if o[0] not in rows:
        rows[o[0]] = [o[1]]
    else:
        rows[o[0]] = rows[o[0]] + [o[1]]
    if o[1] not in cols:
        cols[o[1]] = [o[0]]
    else:
        cols[o[1]] = cols[o[1]] + [o[0]]

print(rows)

def corners_to_edges(c1, c2):
    return [ [c1, [c1[0], c2[1]]],
             [c1, [c2[0], c1[1]]], 
             [c2, [c1[0], c2[1]]],
             [c2, [c2[0], c1[1]]]]

def _to_rows_and_cols(edge):
    return sorted([edge[0][0], edge[1][0]]), sorted([edge[0][1], edge[1][1]])

def edge1_contained_in_edge2(edge1, edge2):
    r1,c1 = _to_rows_and_cols(edge1)
    r2,c2 = _to_rows_and_cols(edge2)
    return r1[0] >= r2[0] and r1[1] <= r2[1] and c1[0] >= c2[0] and c1[1] <= c2[1]

def find_full_range_in_outline(edge):
    r,c = _to_rows_and_cols(edge)
    if r[0] == r[1]:
        all_for_edge = rows[r[0]]
        return [[r[0], min(all_for_edge)], [r[0], max(all_for_edge)]]
    else:
        all_for_edge = cols[c[1]]
        return [[min(all_for_edge), c[0]] , [max(all_for_edge), c[0]]]

def corners_contained(c1, c2):
    edges = corners_to_edges(c1, c2)
    contained = []
    for e in edges:
        ce = find_full_range_in_outline(e)
        contained.append(edge1_contained_in_edge2(e, ce))
    return all(contained)

max_size = 0
for i in range(len(data)):
    for j in range(len(data)):
        if j <= i:
            continue
        if not corners_contained(data[i], data[j]):
            continue
        if data[0] == 96106 or data[1] == 40315:
            continue
        max_size = max([max_size, get_size(data[i], data[j])])

print("Star 2:", max_size)