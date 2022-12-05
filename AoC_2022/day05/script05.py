import re
with open("data05.txt") as d:
    data = [el for el in d.readlines()]
split = data.index("\n")
crane_lines = data[ :split]
instr_lines = data[split+1: ]

class Crane:
    def __init__(self, crane_lines):
        nr_of_stacks = max([int(stack) for stack in re.findall(r'\d+', crane_lines[-1])])
        crane = {}
        for line in crane_lines[:-1]:
            for j in range(1, 4 * nr_of_stacks, 4):
                if line[j] != " ":
                    crane[j // 4 + 1] = crane.get(j // 4 + 1, []) + [line[j]]
        self.crane = crane
    
    def execute_step(self, instr, one_by_one = True):
        nr, f, to = instr
        to_move = self.crane[f][:nr]
        if one_by_one:
            to_move.reverse()
        self.crane[f] = self.crane[f][nr:]
        self.crane[to] = to_move + self.crane[to]
    
    def get_top_boxes(self):
        top = ""
        for i in sorted(self.crane.keys()):
            top = top + self.crane[i][0]
        return top

santa_crane = Crane(crane_lines)

def extract_steps(el):
    return [int(i) for i in re.findall(r'\d+', el)]
instructions = [extract_steps(instr) for instr in instr_lines]

for i in instructions:
    santa_crane.execute_step(i)

print("Star 1 =", santa_crane.get_top_boxes())

santa_crane2 = Crane(crane_lines)
for i in instructions:
    santa_crane2.execute_step(i, one_by_one=False)
print("Star 2 =", santa_crane2.get_top_boxes())