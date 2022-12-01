with open("data08.txt") as d:
    data = d.readlines()
data = [d.split() for d in data]

def process_el(el):
    reg = el[0]
    action = f"+ {el[2]}" if el[1] == "inc" else f"- {el[2]}"
    reg_check = el[4]
    predicate = el[5] + " " + el[6]
    return reg, action, reg_check, predicate

vals = set([d[0] for d in data])

class Collector:
    def __init__(self, values):
        self.coll = dict.fromkeys(values, 0)
        self.max_val = 0
    
    def update_el(self, reg, reg_check, action, predicate):
        c = self.coll
        if eval(str(c[reg_check]) + " " + predicate):
            c[reg] = eval(str(c[reg]) + " " + action)
        self.coll = c
        self.max_val = max(self.max_val, c[reg])

val1 = Collector(vals)
for d in data:
    reg, action, reg_check, predicate = process_el(d)
    val1.update_el(reg, reg_check, action, predicate)
print(f'Star 1: {max(val1.coll.values())}')
print(f'Star 2: {val1.max_val}')

