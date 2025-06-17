import numpy as np
with open("data12.txt") as d:
    data = [line.strip() for line in d.readlines()]

def line_to_nrs(line):
    return [ord(l) - 96 for l in line]

m = np.array([line_to_nrs(l) for l in data])
goal = np.where(m == -27)
m[0,0] = 1
m[goal[0], goal[1]] = 26

class Path:
    def __init__(self, i):
        self.paths = [i]

    def find_adjacent(self, i):
        r,c = i
        s = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
        return [i for i in s if (i[0] >= 0) and (i[1] >= 0) and (i[0] < m.shape[0]) and (i[1] < m.shape[1])]

    def check_reached_finish(self, a):
        return a[0] == goal[0] and a[1] == goal[1]

    def add_steps(self):
        new_paths = []
        for p in self.paths:
            cur_height = m[p[-1][0], p[-1][1]]
            adj = self.find_adjacent(p[-1])
            for a in adj:
                not_visited = a not in p
                good_height = (m[a[0], a[1]] - cur_height) in [0, 1]
                if not_visited and good_height:
                    if self.check_reached_finish(a):
                        print(f"Star 1: {len(p) + 1}")
                        return False
                    new_paths.append(p + [a])
        self.paths = new_paths
        return True
paths = Path([[0,0]])
not_found = True
cnt = 0
while not_found:
   not_found = paths.add_steps()
   cnt += 1
   print(cnt)
   

