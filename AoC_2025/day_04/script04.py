with open('data04.txt') as d:
    data = [el.strip() for el in d.readlines()]

dim = len(data)
def lookaround(d, i, j):
    counter = 0
    i_ls = list(range(max(i-1, 0), min(i+1, dim - 1) + 1))
    j_ls = list(range(max(j-1, 0), min(j+1, dim - 1) + 1))
    for i_l in i_ls:
        for j_l in j_ls:
            if i_l == i and j_l == j:
                continue
            counter += d[i_l][j_l] == '@'
    return counter

counter = 0
for i in range(dim):
    for j in range(dim):        
        if data[i][j] == '@':
            counter += lookaround(data, i, j) < 4

print('Star 1:', counter)

# put data in a list so it is not immutable anymore
data_list = []
for d in data:
    data_list.append([el for el in d])

# set prev_counter to 1 to get while loop going
prev_counter = 1
counter = 0

while counter != prev_counter:
    prev_counter = counter
    for i in range(dim):
        for j in range(dim):        
            if data_list[i][j] == '@':
                nr_around = lookaround(data_list, i, j)
                if nr_around < 4:
                    counter += 1
                    data_list[i][j] = '.'

print('Star 2:', counter)