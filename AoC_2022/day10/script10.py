import numpy as np
with open("data10.txt") as file:
    data = [f.strip() for f in file.readlines()]
X = 1 
cycle = 0 
signal = 0
for d in data:
    if (cycle == 19) or ((cycle - 19) % 40 == 0):
        signal += (cycle + 1) * X
    if d[0] == 'n':
        cycle += 1
    else:
        if (cycle == 18) or ((cycle - 18) % 40 == 0):
            signal += (cycle + 2) * X
        cycle += 2
        X += int(d.split(" ")[1])
print("Star 1 =", signal)
    
X = 1 
image = np.empty([6, 40], dtype=str)
cycle = 0 
row = 0
for d in data:
    if cycle > 39:
        cycle -= 40
        row += 1
    sprite = range(X-1, X+2)
    if d[0] == 'n':
        image[row, cycle] = "#" if cycle in sprite else " "
        cycle += 1
    else:
        for i in range(2):
            image[row, cycle] = "#" if cycle in sprite else " "
            cycle += 1
            if cycle > 39:
                cycle -= 40
                row += 1
        X += int(d.split(" ")[1])

print("Star 2 = ")
for i in range(6):
    print("".join(image[i,]))

