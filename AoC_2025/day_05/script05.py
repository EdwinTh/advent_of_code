with open('data05.txt') as d:
    data = [el.strip() for el in d.readlines()]

ranges = [d.split("-") for d in data if '-' in d]
ranges = [[int(r[0]), int(r[1])] for r in ranges]
ids = [int(d) for d in data if '-' not in d and len(d) > 0]

def is_fresh(id, ranges=ranges):
    for r in ranges:
        if id >= r[0] and id <= r[1]:
            return True
    return False

print("Star 1:", sum([is_fresh(id) for id in ids]))

def range_len(r):
    return r[1] - r[0] + 1

ranges_sorted = sorted(ranges, key= lambda x:x[0])

merged_ranges = []
active_range = ranges_sorted[0]

for r in ranges_sorted:
    if r[1] <= active_range[1]:
        continue
    elif r[0] <= active_range[1]:
        active_range[1] = r[1]
    else:
        merged_ranges.append(active_range)
        active_range = r
merged_ranges.append(active_range)

print("Star 2:", sum([range_len(m) for m in merged_ranges]))

