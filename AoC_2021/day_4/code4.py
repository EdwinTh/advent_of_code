with open('data.txt') as f:
	data = f.readlines()
data = [d.strip() for d in data if d.strip() != '']

nrs = [int(d) for d in data[0].split(",")]

data_split = [d.replace("  ", " ").split(" ") for d in data[1:]]
flattened = [int(el) for row in data_split for el in row]

assert(len(flattened) % 25 == 0)

def nr_to_none(full_list, nr):
	return [None if f == nr else f for f in full_list]

def check_bingo_rows(flattened):
	start_inds = range(0, len(flattened) - 5, 5)
	return([si for si in start_inds if not any(flattened[si:si+5])])
	

def check_bingo_cols(flattened):
	start_inds = [r for r in range(0, len(flattened)) if r % 25 < 5]
	return([si for si in start_inds if not any(flattened[si:si+5])])
	

print(check_bingo_cols(flattened))