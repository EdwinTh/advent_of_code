from math import sqrt, floor
import numpy as np

input_val = 325489

root = floor(sqrt(input_val))
if root % 2 == 0:
    root -= 1

base_val  = (root - 1) // 2 + 1

val = root * root
steps = input_val - val
side_len = root + 1
steps_to_corners = np.cumsum(np.array([side_len * 3]))
sides = sum(steps >= steps_to_corners)
steps_from_corner = steps - steps_to_corners
if sides == 0:
    ind = (base_val, -base_val - 1 + steps)
elif sides == 1:
    ind = (base_val - steps_from_corner[0], base_val)
elif sides == 2:
    ind = (-base_val, base_val - steps_from_corner[1])
else:
    ind = (-base_val + steps_from_corner[2], -base_val)
print("The value for star 1 is " + str(sum(abs(i) for i in ind)))

def add_ring(start_coord = (1, 0), first_val = 2):
    side_len = start_coord[0] * 2
    coord_1print(list(range(start_coord[1], start_coord[1] + side_len)))

add_ring()
