import string

POINTS_LOOKUP = dict(
    zip(
        list(string.ascii_lowercase) + list(string.ascii_uppercase), 
        list(range(1,53)))
    )

with open('data03.txt') as d:
    data = [el.strip() for el in d.readlines()]

def split_on_half(el):
    el1 = el[ :(len(el) // 2)]
    el2 = el[len(el) // 2:]
    return el1, el2

def find_common_letter(el1, el2):
    return set(el1).intersection(set(el2))

def find_points(el):
    half1, half2 = split_on_half(el)
    letter = find_common_letter(half1, half2)
    return POINTS_LOOKUP[list(letter)[0]]

print("Star 1 =", sum([find_points(d) for d in data]))

ds = [set(d) for d in data]

def find_common(s1, s2, s3):
    return list(s1.intersection(s2).intersection(s3))[0]

letters_common = []
for i in range(1, len(ds) + 1):
    if i % 3 == 0:
        letters_common.append(
            find_common(ds[i-3], ds[i-2], ds[i-1])
        )
points2 = [POINTS_LOOKUP[l] for l in letters_common]
print("Star 2 =", sum(points2))
