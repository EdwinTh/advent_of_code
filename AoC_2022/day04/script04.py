with open("data04.txt") as d:
    data = [el.strip().split(",") for el in d.readlines()]

def split_el(el):
    ret = [el[0].split("-"), el[1].split("-")]
    return [[int(ret[0][0]), int(ret[0][1])], [int(ret[1][0]), int(ret[1][1])]]

def sort_els(el):
    if el[0][0] < el[1][0]:
        return el
    elif (el[0][0] == el[1][0]) and (el[0][1] > el[1][1]):
        return el
    else:
        return [el[1], el[0]]

def second_contained_by_first(el):
    return (el[0][0] <= el[1][0]) and (el[0][1] >= el[1][1])

sorted = [sort_els(split_el(d)) for d in data]
contained = [second_contained_by_first(el) for el in sorted]

print("Star 1 =", sum(contained))

def do_overlap(el):
    return el[0][1] >= el[1][0]

ovelaped = [do_overlap(el) for el in sorted]

print("Star 2 =", sum(ovelaped))