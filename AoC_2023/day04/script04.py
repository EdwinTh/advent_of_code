import re
with open('data04.txt') as d:
    data = [el.strip() for el in d.readlines()]

data_splitted = [d.split(":")[1].split("|") for d in data]

def clean_nrs(string):
    return [int(dig) for dig in re.findall("\d+", string)]

data_cleaned = [ [clean_nrs(ds[0]), clean_nrs(ds[1])] for ds in data_splitted]  

def get_score(dc):
    score = 0
    for nr in dc[0]:
        if nr in dc[1]:
            score = max(1, score*2)
    return score
print("Star 1:", sum([get_score(dc) for dc in data_cleaned]))

rep_dict = {i:1 for i in range(1, len(data_cleaned) + 1)}

def get_hits(dc):
    hits = 0
    for nr in dc[0]:
        if nr in dc[1]:
            hits += 1
    return hits

for i in range(1, len(data_cleaned) + 1):
    hits = get_hits(data_cleaned[i-1])
    if hits > 0 and i < len(data_cleaned)+1:
        for j in range(i+1, i+hits+1):
            rep_dict[j] += rep_dict[i]

print("Star 2:", sum(rep_dict.values()))


    