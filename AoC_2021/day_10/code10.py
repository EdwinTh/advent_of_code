data = [e.strip() for e in open('data10.txt')]

# star 1
expected = {'[':']' , '{':'}', '<':'>', '(':')'}
values = {']': 57, '}':1197, '>':25137, ')':3}

def find_corrupt(el, exp):
    exp_close = []
    for char in el:
        if char in exp.values():
            if char != exp_close[-1]:
                return char
            else:
                exp_close = exp_close[:-1]
        else: 
            exp_close.append(exp[char])
        
corrupt = [find_corrupt(el, expected) for el in data]
print(corrupt)
score = [values[c] for c in corrupt if c is not None]
print(sum(score))

# star 2
values2 = {']': 2, '}':3, '>':4, ')':1}
non_cor = [data[i] for i in range(len(data)) if corrupt[i] is None]

def find_remainder(el, exp):
    exp_close = []
    for char in el:
        if char in exp.values():
            exp_close = exp_close[:-1]
        else: 
            exp_close.append(exp[char])
    exp_close.reverse()
    return exp_close

remainders = [find_remainder(nc, expected) for nc in non_cor]

def get_score(rem, vals):
    score = 0
    for c in rem:
        score = score * 5 + vals[c]
    return score

scores = [get_score(rem, values2) for rem in remainders]
scores.sort()
print(scores[len(scores) / 2])
