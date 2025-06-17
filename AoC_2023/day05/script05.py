import re
with open('data05.txt') as d:
    data = [el.strip() for el in d.readlines()]

seeds = [int(d) for d in re.findall("\d+", data[0])]

def process_mapping(input):
    spl = [int(s) for s in input.split(" ")]
    dest = range(spl[0], spl[0] + spl[2])
    src = range(spl[1], spl[1] + spl[2])
    return src, dest

all_mappings = []
mapping = []
for i in range(1, len(data)):
    if len(data[i]) > 0:
        if data[i][0].isnumeric():
            mapping.append(data[i])
        else:
            if len(mapping) > 0:
                mapping = [process_mapping(m) for m in mapping]
                all_mappings.append(mapping)
                mapping = []
mapping = [process_mapping(m) for m in mapping]
all_mappings.append(mapping)

def find_to_val_mapping(val, mapping):
    if val in mapping[0]:
        ind = mapping[0].index(val)
        return mapping[1][ind]

def find_to_val_mapping_list(val, mapping_list):
    found = None
    for mapping in mapping_list:
        found = find_to_val_mapping(val, mapping)
        if found is not None:
            return found
    return val

def seed_to_location(val):
    for i in range(len(all_mappings)):
        val = find_to_val_mapping_list(val, all_mappings[i])
    return val

print("Star 1: ", str(min([seed_to_location(seed) for seed in seeds])))

seeds2 = []
for i in range(0, len(seeds), 2):
    seeds2.append(range(seeds[i], seeds[i] + seeds[i+1]))

def find_from_val_mapping(val, mapping):
    if val in mapping[1]:
        ind = mapping[1].index(val)
        return mapping[0][ind]

def find_from_val_mapping_list(val, mapping_list):
    found = None
    for mapping in mapping_list:
        found = find_from_val_mapping(val, mapping)
        if found is not None:
            return found
    return val

def location_to_seed(val):
    for i in range(len(all_mappings)-1, -1, -1):
        val = find_from_val_mapping_list(val, all_mappings[i])
    return val

def closing_in(start_val, step_size):
    val = start_val
    while True:
        seed = location_to_seed(val)
        if any([seed in seeds for seeds in seeds2]):
            break
        val += step_size
    return val - step_size

start_val = 0
step_sizes = [10**i for i in range(8, -1, -1)]

for step_size in step_sizes:
    start_val = closing_in(start_val, step_size)

print("Star 2: ", str(start_val + 1))