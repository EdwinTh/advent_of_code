from copy import deepcopy
with open('data06.txt') as d:
    data = [el.strip() for el in d.readlines()]

class Grid:
    def __init__(self, data):
        self.data = deepcopy(data)
        self.grid_size = len(data[0]) - 1

    def find_start_val(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == "^":
                    return [i, j]

    def return_value(self, pos):
        if pos[0] < 0 or pos[1] < 0 or pos[0] > self.grid_size or pos[1] > self.grid_size:
            return False
        return self.data[pos[0]][pos[1]]

    def get_all_free_positions(self):
        free_postions = []
        for i in range(self.grid_size + 1):
            for j in range(self.grid_size + 1):
                if self.data[i][j] == ".":
                    free_postions += [[i, j]]
        return free_postions

    def change_to_blocked(self, pos):
        row = self.data[pos[0]]
        new_row = row[:pos[1]] + "#" + row[pos[1]+1:]
        self.data[pos[0]] = new_row


class Guard:
    def __init__(self, start_pos, max_steps=10000):
        self.route = []    
        self.position = start_pos
        self.direction = "up"
        self.steps_cnt = 0
        self.max_steps = max_steps
    
    def _next(self):
        if self.direction == "up":
            return [self.position[0] - 1, self.position[1]]
        elif self.direction == "down":
            return [self.position[0] + 1, self.position[1]]
        elif self.direction == "left":
            return [self.position[0], self.position[1] - 1]
        elif self.direction == "right":
            return [self.position[0], self.position[1] + 1]

    def _change_direction(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "up"
        elif self.direction == "right":
            self.direction = "down"
            
    def walk(self, grid):
        while True:
            self.steps_cnt += 1
            next_step = self._next()
            next_val = grid.return_value(next_step)
            if not next_val or self.steps_cnt == self.max_steps:
                self.route += [self.position]
                break
            if next_val in [".", "^"]:
                self.route += [self.position]
                self.position = next_step
            else:
                self._change_direction()
        
    def did_not_exit(self):
        return self.steps_cnt == self.max_steps


grid = Grid(data)
guard = Guard(grid.find_start_val())
guard.walk(grid)
print('Star 1:', str(len(set(str(l[0])+'-'+str(l[1]) for l in guard.route))))

all_free_positions = grid.get_all_free_positions()
not_exited = []
for pos in all_free_positions:
    grid = Grid(data)
    grid.change_to_blocked(pos)
    guard = Guard(grid.find_start_val())
    guard.walk(grid)
    if guard.did_not_exit():
        not_exited += [pos]

print('Star 2:', str(len(not_exited)))
    


