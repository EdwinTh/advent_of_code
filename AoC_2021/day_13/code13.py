from itertools import product
# star 1
data = [el.strip() for el in open('data.txt') if el.strip() != '']
c = [el.split(',') for el in data if el[0].isdigit()]
c = [(int(x), int(y)) for x,y in c]
steps = [el.split('=') for el in data if not el[0].isdigit()]
steps = [[dim[-1], int(nr)] for dim, nr in steps]

def y_fold(c, dim):
    new_c_below = [(x, dim - (y - dim)) for x, y in c if y > dim]
    new_c = [(x,y) for x,y in c if y < dim] + new_c_below
    return set(new_c)

def x_fold(c, dim):
    new_c_right = [(dim - (x - dim), y) for x, y in c if x > dim]
    new_c = [(x,y) for x,y in c if x < dim] + new_c_right
    return set(new_c)

def take_step(c, step):
    if step[0] == 'y':
        return y_fold(c, step[1])
    return x_fold(c, step[1])

print(len(take_step(c, steps[0])))
    
# star 2
for s in steps:
    c = take_step(c, s)
max_x = max([x for x, y in c])
max_y = max([y for x, y in c])

for y in range(max_y + 1):
    line = ['#' if (x, y) in c else ' ' for x in range(max_x + 1)]
    print(''.join(line))
