
with open('data09.txt') as d:
    data = [el.strip() for el in d.readlines()][0]

def input_to_blocks(input):
    block = []
    id = 0
    empty = False
    for i in input:
        if empty:
            block += ["."] * int(i)
            empty = False
        else:
            block += [id] * int(i)
            id += 1
            empty = True
    return block

def reshuffle_elements(input):
    non_empty_reversed = [i for i,el in enumerate(input) if el != '.'][::-1]
    empty = [i for i,el in enumerate(input) if el == '.']
    combs = [(e, non_empty_reversed[i]) for i,e in enumerate(empty) if e < non_empty_reversed[i]]
    for c in combs:
        input[c[0]], input[c[1]] = input[c[1]], input[c[0]]
    return input

def calculate_checksum(input):
    return sum([i * int(nr) for i,nr in enumerate(input) if nr != '.'])

blocks = input_to_blocks(data)
reshuffled = reshuffle_elements(blocks)

print('Star 1:', calculate_checksum(reshuffled))

def input_to_blocks_key_value(input):
    block = []
    block_kv = {}
    id = 0
    empty = False
    for i in input:
        if empty:
            if i != "0":
                block += [{"val" : ".", "reps" : int(i)}]
            empty = False
        else:
            if i != "0":
                block += [{"val" : id, "reps" : int(i)}]
                block_kv[id] = int(i)
            id += 1
            empty = True
    return block, block_kv

def find_first_empty_block(input, size):
    for i,inp in enumerate(input):
        if inp['val'] == '.' and inp['reps'] >= size:
            return i
    return None

def place_block_on_empty_space(input, ind, value, reps):
    before = input[:ind]
    after = input[ind+1:]
    insert = [{'val':value, 'reps':reps}]
    if reps < input[ind]['reps']:
        insert += [{'val':'.', 'reps':input[ind]['reps']-reps}]
    return before + insert + after


def flatten_blocks(blocks):
    inner_lists =  [[x['val']] * x['reps'] for x in blocks]
    flat_list = []
    for inner_list in inner_lists:
        for el in inner_list:
            flat_list.append(el)
    return flat_list


def reshuffle_blocks(blocks, blocks_kv):
    for id in list(blocks_kv.keys())[::-1]:
        reps = blocks_kv[id]
        ind = find_first_empty_block(blocks, reps)
        current_ind = min([nr for nr,val in enumerate(flatten_blocks(blocks)) if val == id])
        if ind is not None and ind < current_ind:
            blocks = [{'val':'.', 'reps':d.get("reps")} if d.get('val') == id else d for d in blocks]
            blocks = place_block_on_empty_space(blocks, ind, id, reps)
    return blocks

blocks, blocks_kv = input_to_blocks_key_value(data)
blocks = reshuffle_blocks(blocks, blocks_kv)
print('Star 2:', calculate_checksum(flatten_blocks(blocks)))

