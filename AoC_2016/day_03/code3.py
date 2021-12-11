data = [el.strip().split() for el in open('data3.txt')]

def valid_tri(el):
    ints = [int(e) for e in el]
    ints.sort()
    return ints[2] < sum(ints[:2])

valid_tris = [valid_tri(el) for el in data]
print(sum(valid_tris))

valid_tris = []
for i in range(3):
    for j in range(len(data)):
        if j % 3 == 0:
            valid_tris.append(valid_tri([data[j][i]] + [data[j+1][i]] + [data[j+2][i]]))
print(sum(valid_tris))