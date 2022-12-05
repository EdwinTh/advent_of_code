with open('data01.txt') as d:
    data = [el.strip() for el in d.readlines()]

data_dict = {}
elf = 1
for d in data:
    if d == "":
        elf += 1
    else:
        data_dict[elf] = data_dict.get(elf, 0) + int(d)

print("Star 1 =", max(data_dict.values()))
print("Star 2 =" ,sum(sorted(data_dict.values())[-3:]))
