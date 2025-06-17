import re
with open('data02_test.txt') as d:
    data = [re.findall("\d+", el.strip()) for el in d.readlines()]

def deem_safe(nrs):
    to_int = [int(nr) for nr in nrs]
    difs = [to_int[i] - to_int[i-1] for i in range(1, len(to_int))]
    all_neg = all([d < 0 and d > -4 for d in difs])
    all_pos = all([d > 0 and d < 4 for d in difs])
    return all_neg or all_pos

safe = [deem_safe(d) for d in data]
print("Star 1:", sum(safe))

def deem_safe_with_dampener(nrs):
    is_safe = deem_safe(nrs)
    omit = 0
    while not is_safe and omit < len(nrs):
        nrs_iter = [n for i,n in enumerate(nrs) if i != omit]
        is_safe = deem_safe(nrs_iter)
        omit += 1
    return is_safe

safe = [deem_safe_with_dampener(d) for d in data]
print("Star 2:", sum(safe))
