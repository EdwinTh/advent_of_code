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


class Cell:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def print(self):
        print(f"x = {self.x}, y = {self.y}, value = {self.value}")

class Grid:
    def __init__(self):
        self.grid = [Cell(0, 0, 1)]
        self.current_index = (0, 0)
        self.indices_visited = [(0, 0)]
        self.dir = "right"

    def _get_next_in_dir(self, dir):
        if dir == "right":
            return (self.current_index[0], self.current_index[1] + 1)
        if dir == "up":
            return (self.current_index[0] + 1, self.current_index[1])
        if dir == "left":
            return (self.current_index[0], self.current_index[1] - 1)
        if dir == "down":
            return (self.current_index[0] - 1, self.current_index[1])

    def _update_index_and_dir(self):
        if self.current_index == (0, 0):
            self.current_index = (0, 1)
        elif self.dir == "right":
            if self._get_next_in_dir("up") not in self.indices_visited:
                self.current_index = self._get_next_in_dir("up")
                self.dir = "up"
            else:
                  self.current_index = self._get_next_in_dir("right")
        elif self.dir == "up":
            if self._get_next_in_dir("left") not in self.indices_visited:
                self.current_index = self._get_next_in_dir("left")
                self.dir = "left"
            else:
                  self.current_index = self._get_next_in_dir("up")
        elif self.dir == "left":
            if self._get_next_in_dir("down") not in self.indices_visited:
                self.current_index = self._get_next_in_dir("down")
                self.dir = "down"
            else:
                  self.current_index = self._get_next_in_dir("left")
        elif self.dir == "down":
            if self._get_next_in_dir("right") not in self.indices_visited:
                self.current_index = self._get_next_in_dir("right")
                self.dir = "right"
            else:
                  self.current_index = self._get_next_in_dir("down")


    def _get_adjacent_values(self, x, y):
        values = []
        for cell in self.grid:
            if abs(cell.x - x) in (0,1) and abs(cell.y - y) in (0,1):
                values += [cell.value]
        return values

    def _add_cell(self, cell):
        self.grid += [cell]

    def update_grid(self):
        self._update_index_and_dir()
        values = self._get_adjacent_values(self.current_index[0], self.current_index[1])
        self._add_cell(Cell(self.current_index[0], self.current_index[1], sum(values)))
        self.indices_visited += [(self.current_index[0], self.current_index[1])]

    def update_until_value_reached(self, value):
        while self.grid[-1].value < value:
            self.update_grid()
        
g = Grid()
g.update_until_value_reached(input_val)
print("The value for star 2 is", str(g.grid[-1].value))