with open('data02.txt') as d:
    data = [el.strip().split(",") for el in d.readlines()][0]
    data = [el.split('-') for el in data]

def el_to_range(el):
    return list(range(int(el[0]), int(el[1])+1))

all_ids = []
for el in data:
    all_ids += el_to_range(el)

def is_repeating(id):
    id_str = str(id)
    if len(id_str) % 2 == 1:
        return False
    return id_str[:len(id_str) // 2] == id_str[len(id_str) // 2:]

print("Star 1:", sum([id for id in all_ids if is_repeating(id)]))

def check_repeat_invalid(id_str, rep):
    if len(id_str) % rep != 0 or len(id_str) == rep:
        return False
    first_part = id_str[:rep]
    for i in range(1, len(id_str) // rep):
        check_part = id_str[rep*i:rep*(i+1)]
        if first_part != check_part:
            return False
    return True

def is_invalid(id):
    id_str = str(id)
    reps_to_check = list(range(1, (len(id_str)) // 2 + 1))
    return any([check_repeat_invalid(id_str, i) for i in reps_to_check])

print("Star 2:", sum([id for id in all_ids if is_invalid(id)]))
