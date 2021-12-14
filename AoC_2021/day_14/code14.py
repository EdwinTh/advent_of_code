from collections import Counter
# star 1
data = [el.strip() for el in open('data.txt')]
polymer = data[0]
mapping = dict([m.split(' -> ') for m in data[2:]])

def insert(p, m):
    to_insert = [m[p[i:i+2]] for i in range(len(p)-1)] + [""]
    return "".join([p[i] + to_insert[i] for i in range(len(p))])

for i in range(10):
    polymer = insert(polymer, mapping)

cnts = Counter(polymer).values()
print(max(cnts) - min(cnts))

# star 2
polymer =  data[0]
combs = Counter([polymer[i:i+2] for i in range(len(polymer)-1)])
def comb_to_new_combs(comb, nr, m):
    ins = m[comb]
    return Counter({comb[0] + ins:nr, ins + comb[1]: nr})

def one_step(combs, mapping):
    new_combs = Counter()
    for k,v in combs.iteritems():
        new_combs = new_combs + comb_to_new_combs(k, v, mapping)
    return new_combs

for _ in range(40):
    combs = one_step(combs, mapping)

def wrap_to_letters(k, v):
    if k[0] == k[1]:
        return Counter({k[0]:v*2})
    return Counter({k[0]:v, k[1]:v})
     
letters = Counter()
for k,v in combs.iteritems():
    letters = letters + wrap_to_letters(k, v)

letters[polymer[0]] = letters[polymer[0]] + 1
letters[polymer[-1]] = letters[polymer[-1]] + 1
print(max(letters.values()) / 2 - min(letters.values()) / 2) 