import re
from copy import deepcopy
with open('data10.txt') as d:
    data = [el.strip() for el in d.readlines()]

def get_end_state(d):
    return re.search('\[(.+?)\]', d).group(1)

def switch_to_ints(switch):
    els = re.search('\((.+?)\)', switch).group(1).split(',')
    return [int(el) for el in els]

def get_switches(d):
    switches = re.search('\](.+?)\{', d).group(1)
    splitted = switches.strip().split(" ")
    return [switch_to_ints(switch) for switch in splitted]

def make_switch(state, switch):
    state_list = list(state)
    for s in switch:
        state_list[s] = "." if state_list[s] == "#" else "#"
    return "".join(state_list)

class Machine:
    def __init__(self, d):
        self.end_state = get_end_state(d)
        self.switches = get_switches(d)
        self.states = ["." * len(self.end_state)]
        self.iterations = 0

    def iteration(self):
        new_states = []
        for state in self.states:
            for switch in self.switches:
                new_states += [make_switch(state, switch)]
        self.states = new_states

    def iterate_untill_end_state(self):
        while True:
            if any([state == self.end_state for state in self.states]):
                break
            self.iteration()
            self.iterations += 1

#iterations = 0
#for d in data:
#    m = Machine(d)
#    m.iterate_untill_end_state()
#    iterations += m.iterations#

#print("Star 1:", iterations)

def get_joltage(d):
    joltages = re.search('\{(.+?)\}', d).group(1)
    return [int(j) for j in joltages.split(",")]


def switch_joltage(joltage, switch):
    j = deepcopy(joltage)
    for s in switch:
        j[s] += 1
    return j

class Machine2:
    def __init__(self, d):
        self.joltage = get_joltage(d)
        self.switches = get_switches(d)
        self.joltages = [[0 for r in self.joltage]]
        self.iterations = 0

    def iteration(self):
        new_joltages = []
        for j in self.joltages:
            for switch in self.switches:
                new_joltages += [switch_joltage(j, switch)]
        self.joltages = new_joltages

    def prune(self):
        joltages_remainig = []
        for j in self.joltages:
            if all( [j[i] <= self.joltage[i] for i in range(len(j))] ):
                joltages_remainig += [j]
        self.joltages = joltages_remainig

    def distinct_joltages(self):
        unique_joltages = [list(x) for x in set(tuple(x) for x in self.joltages)]
        self.joltages = unique_joltages

    def iterate_untill_end_state(self):
        while True:
            if any([joltage == self.joltage for joltage in self.joltages]):
                break
            self.iteration()
            self.distinct_joltages()
            self.prune()
            self.iterations += 1
            print(self.iterations)

        
iterations = 0
i = 1
for d in data:
    m = Machine2(d)
    m.iterate_untill_end_state()
    iterations += m.iterations
    print(i)
    i += 1


print("Star 2:", iterations)
