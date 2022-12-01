with open("data09.txt") as d:
    data = d.read()

total = 0
score = 0
skip = False
garbage = False
coll = 0
for c in data:
    if skip:
        skip = False
        continue
    if c == "!":
        skip = True
    elif garbage and c == "<":
        coll += 1
    elif c == "<":
        garbage = True
    elif garbage and c == ">":
        garbage = False
    elif garbage:
        coll += 1
    elif c == '{':
        score += 1
    elif c == '}':
        total += score
        score -= 1
print('star1:', total) 
print('star2:', coll) 