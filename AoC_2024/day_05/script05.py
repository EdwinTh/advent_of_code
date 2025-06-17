with open('data05.txt') as d:
    data = [el.strip() for el in d.readlines()]

orders = []
prints = []
add_orders = True
for d in data:
    if d == "":
        add_orders = False
        continue
    if add_orders:
        orders.append(d)
    else:
        prints.append(d)
    
order_dict = {}
for order in orders:
    spl = order.split("|")
    if spl[0] not in order_dict:
        order_dict[spl[0]] = [spl[1]]
    else:
        order_dict[spl[0]] = order_dict[spl[0]] + [(spl[1])]

prints = [p.split(",") for p in prints]
def valid_print(p):
    for i in range(1, len(p)):
        if p[i] not in order_dict:
            continue
        not_before = order_dict[p[i]]
        for p_before in p[:i]:
            if p_before in not_before:
                return False
    return True

is_valid = [valid_print(p) for p in prints]
middle_of_valids = [int(p[int(len(p)/2)]) for p,v in zip(prints, is_valid) if v]

print("Star 1:", sum(middle_of_valids))

def put_in_right_order(value, l):
    if len(l) == 0:
        return [value]
    for i in range(len(l)):
        if l[i] in order_dict:
            if value in order_dict[l[i]]:
                continue
        l.insert(i, value)
        return l
    l.append(value)
    return l

def reorder_list(l):
    new_l = []
    for v in l:
        new_l = put_in_right_order(v, new_l)
    return new_l

reordered = [reorder_list(pr) for pr,v in zip(prints, is_valid) if not v]
middle = [int(p[int(len(p)/2)]) for p in reordered]

print("Star 2:", sum(middle))