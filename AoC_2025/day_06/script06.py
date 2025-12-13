from math import prod
with open('data06.txt') as d:
    data = [el.strip().split(" ") for el in d.readlines()]

data = [[e for e in el if e != ''] for el in data]
results = []
for i in range(len(data[0])):
    ints = []
    for j in range(len(data)-1):
        ints.append(int(data[j][i]))
    if data[len(data)-1][i] == "+":
        results.append(sum(ints))
    else:
        results.append(prod(ints))

print("Star 1:", sum(results))

with open('data06.txt') as d:
    data = [el for el in d.readlines()]

break_ind = []
for i in range(len(data[0])-1):
    pos_i_data = [data[j][i] for j in range(len(data)-1)]
    if all([p == " " for p in pos_i_data]):
        break_ind.append(i)


data_rearranged = []
data_iter = []
for i in range(len(data[0])-1):
    if i in break_ind:
        data_rearranged.append(data_iter)
        data_iter = []
    else:
        int_iter = []
        for j in range(len(data)-1):
            int_iter.append(data[j][i])
        data_iter.append(int("".join(int_iter)))
data_rearranged.append(data_iter)

operators = [d.strip() for d in data[(len(data))-1].split(" ")]
operators = [o for o in operators if o != ""]

results = []
for i in range(len(operators)):
    if operators[i] == "+":
        results.append(sum(data_rearranged[i]))
    else:
        results.append(prod(data_rearranged[i]))

print("Star 2:", sum(results))
