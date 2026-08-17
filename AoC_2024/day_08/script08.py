from itertools import product
with open('./data08.txt') as d:
    data = [el.strip() for el in d.readlines()]

matrix = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        matrix[str(i) + '-' + str(j)] = data[i][j]

def look_direction(matrix, start_i, start_j, up_down, left_right):
    ret_list = []
    ret_list.append(matrix[str(start_i) + '-' + str(start_j)])
    i = start_i + up_down
    j = start_j + left_right
    ind = str(i) + '-' + str(j)
    while ind in matrix:
        ret_list.append(matrix[ind])
        i += up_down
        j += left_right
        ind = str(i) + '-' + str(j)
    return ret_list

def is_antinode_v(direction, v):
    inds_v = [i for i,d in enumerate(direction) if d == v]
    inds_v_rev = list(reversed(inds_v))
    if len(inds_v) > 1:
        for i in range(len(inds_v)):
            for j in range(i, len(inds_v)):
                if inds_v_rev[j] != 0:
                    if inds_v_rev[i] / inds_v_rev[j] == 2:
                        return True 
    return False

def is_antinode(direction):
    values = set(direction)
    for v in values:
        if v == '.':
            continue
        if is_antinode_v(direction, v):
            return True
    return False

class Spot:
    def __init__(self, i, j, matrix, data):
        self.i = i
        self.j = j
        self.matrix = matrix
        self.n_i = int(len(data[0]) -1)
        self.n_j = int(len(data) - 1)

    def _possible_directions(self):
        left_right = range(-self.i // 2, (self.n_i - self.i) // 2)
        up_down = range(-self.j // 2, (self.n_j - self.j) // 2)
        self.possible_directions = list(product(list(left_right), list(up_down)))
        if (0,0) in self.possible_directions:
            self.possible_directions.remove((0,0))

    def is_antinode(self):
        self._possible_directions()
        for pd in self.possible_directions:
            direction = look_direction(self.matrix, self.i, self.j, pd[0], pd[1])
            if is_antinode(direction):
                return True
        return False

antinodes = []
for i in range(len(data)):
    for j in range(len(data[i])):
        antinode = Spot(int(i), int(j), matrix, data).is_antinode()
        antinodes += [antinode]

print("Star 1:", sum(antinodes))
