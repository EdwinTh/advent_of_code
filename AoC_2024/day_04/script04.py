with open('data04.txt') as d:
    data = [el.strip() for el in d.readlines()]

max_x = len(data[0])
max_y = len(data)

def subset(x_coords, y_coords):
    if any([x < 0 for x in x_coords]) or any([y < 0 for y in y_coords]):
        return None
    if any([x >= max_x for x in x_coords]) or any([y >= max_y for y in y_coords]):
        return None
    chars = ""
    for x,y in zip(x_coords, y_coords):
        chars += data[y][x]
    return chars

def lookaround(x, y):
    around = []    
    indices = [ 
        [[x]*4, range(y, y-4, -1)], 
        [[x]*4, range(y, y+4)],
        [range(x, x-4, -1), [y]*4], 
        [range(x, x+4), [y]*4],
        [range(x, x-4, -1), range(y, y-4, -1)],
        [range(x, x-4, -1), range(y, y+4)],
        [range(x, x+4), range(y, y-4, -1)],
        [range(x, x+4), range(y, y+4)],
    ]
    for ind in indices:
        around.append(subset(ind[0], ind[1]))
    return around

def count_XMAS(around):
    return len([a for a in around if a == 'XMAS'])

cnt = 0
for i in range(len(data[0])):
    for j in range(len(data)):
        if data[j][i] == "X":
            cnt += count_XMAS(lookaround(i,j))

print("Star 1:", cnt)

def check_X_MAS(x, y):
    if x + 3 > max_x or y + 3 > max_y:
        return 0
    left_right = subset(range(x, x+3), range(y, y+3))
    right_left = subset(range(x, x+3), range(y+2, y-1, -1))
    return int(left_right in ['MAS', 'SAM'] and right_left in ['MAS', 'SAM'])

cnt = 0
for i in range(len(data[0])):
    for j in range(len(data)):
        cnt += check_X_MAS(i, j)
    
print("Star 2:", cnt)