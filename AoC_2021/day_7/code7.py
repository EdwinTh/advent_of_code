with open('data7.txt') as f:
    data = f.readlines()
data = [int(d) for d in data[0].split(",")]

# star 1
amount = []
for i in range(min(data), max(data)):
    amount.append(sum([abs(i - pos) for pos in data]))

print(min(amount))

# star 2
def fuel_pos(a, b):
    dif = abs(a-b)
    return (pow(dif, 2) - dif) / 2 + dif

amount = []
for i in range(min(data), max(data)):
    amount.append(sum([fuel_pos(i,pos) for pos in data]))

print(min(amount))