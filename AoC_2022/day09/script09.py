with open("data09.txt") as file:
    data = [[f.split()[0], int(f.split()[1])] for f in file.readlines()]

h_steps = "".join([l[0] * l[1] for l in data])

class Rope:
    def __init__(self, knots = 2):
        self.k = [[0,0] for i in range(knots)]
        self.tail_visited = {'0,0'}

    def move_head(self, d):
        if d == "U": self.k[0][1] += 1
        if d == "D": self.k[0][1] -= 1
        if d == "R": self.k[0][0] += 1
        if d == "L": self.k[0][0] -= 1
    
    def _move_one_knot(self, p):
        difx = self.k[p-1][0] - self.k[p][0]
        dify = self.k[p-1][1] - self.k[p][1]
        if abs(difx) == 2 or (abs(dify) == 2 and abs(difx) == 1):
            self.k[p][0] = self.k[p][0] + 1 if difx > 0 else self.k[p][0] - 1
        if abs(dify) == 2 or (abs(difx) == 2 and abs(dify) == 1):
            self.k[p][1] = self.k[p][1] + 1 if dify > 0 else self.k[p][1] - 1
    
    def move_knots(self):
        for i in range(1, len(self.k)):
            self._move_one_knot(i)

    def update_tail_visited(self):
        self.tail_visited = set(list(self.tail_visited) + [f'{self.k[-1][0]},{self.k[-1][1]}'])

r = Rope()
for s in h_steps:
    r.move_head(s)
    r.move_knots()
    r.update_tail_visited()
print("Star 1 =", len(r.tail_visited))

r = Rope(10)
for s in h_steps:
    r.move_head(s)
    r.move_knots()
    r.update_tail_visited()
print("Star 2 =", len(r.tail_visited))