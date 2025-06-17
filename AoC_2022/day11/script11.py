import re
with open("data11.txt") as file:
    data = [f.strip() for f in file.readlines()]

raws = [data[i*7:i*7+7] for i in range((len(data) + 1) // 7)]

class Monkey:
    def __init__(self, raw):
        self.nr = re.findall(r"\d+", raw[0])[0]
        self.items = [int(i) for i in re.findall(r"\d+", raw[1])]
        self.operation = raw[2].split("= ")[1]
        self.test = int(re.findall(r"\d+", raw[3])[0])
        self.true = re.findall(r"\d+", raw[4])[0]
        self.false = re.findall(r"\d+", raw[5])[0]
        self.items_inspected = []

    def get_worry(self):
        wlev = f'({self.operation}) // 3'
        wlev = wlev.replace("old", str(self.items[0]))
        return eval(wlev)

    def get_receiver(self, worry):
        return self.true if worry % self.test == 0 else self.false

    def throw(self):
        self.items.pop(0)

    def receive(self, pack):
        self.items.append(pack)

    def inspect(self):
        self.items_inspected.append(self.items)

    def play_round(self):
        items_to_throw = [[], []]
        while len(self.items) > 0:
            self.inspect()
            worry = self.get_worry()
            to = self.get_receiver(worry)
            items_to_throw[0].append(to)
            items_to_throw[1].append(worry)
            self.throw()
        return items_to_throw

monkeys = {}
for m in raws:
    monkey = Monkey(m)
    monkeys[monkey.nr] = monkey

def play_round():
    for m in sorted(monkeys.keys()):
        to_throw = monkeys[m].play_round()
        for i in range(len(to_throw[0])):
            monkeys[to_throw[0][i]].receive(to_throw[1][i])

for i in range(20): play_round()

items_held = sorted([len(monkeys[str(i)].items_inspected) for i in range(len(monkeys))])
print("Star 1 =", items_held[-2] * items_held[-1])
