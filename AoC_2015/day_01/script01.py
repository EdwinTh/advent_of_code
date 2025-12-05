with open('data01.txt') as d:
    data = [el.strip() for el in d.readlines()][0]

floor = 0
for d in data:
    if d == '(':
        floor += 1
    else:
        floor -= 1

print("Star 1:", floor)

floor = 0
cnt = 0
for d in data:
    cnt += 1
    if d == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        break

print("Star 2:", cnt)