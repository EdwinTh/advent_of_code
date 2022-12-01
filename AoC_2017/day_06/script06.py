import re
with open("data06.txt") as d:
    data = d.read()
nrs = [int(el) for el in re.findall("\d+", data)]
iters = ["-".join([str(nr) for nr in nrs])]

def update(nrs):
    max_ind = nrs.index(max(nrs))
    val = nrs[max_ind]
    nrs[max_ind] = 0
    update = max_ind + 1
    while val > 0:
        if update == len(nrs):
            update = 0
        nrs[update] += 1
        val -= 1
        update += 1
    return nrs

while True:
    nrs = update(nrs)
    iters.append("-".join([str(nr) for nr in nrs]))
    if len(iters) - len(set(iters)) == 1:
        break
print("Star 1: ", str(len(set(iters))))

iters = ["-".join([str(nr) for nr in nrs])]
while True:
    nrs = update(nrs)
    iters.append("-".join([str(nr) for nr in nrs]))
    if len(iters) - len(set(iters)) == 1:
        break
print("Star 2: ", str(len(set(iters))))