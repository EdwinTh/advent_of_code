with open("data13.txt") as file:
    data = [d.strip() for d in file.readlines()]
pairs = [data[i*3:i*3+2] for i in range(len(data) // 3)]

def equalize(l, r):
    if len(l) < len(r):
        l = l + [0 for i in range(len(r) - len(l))]
    elif len(l) > len(r):
        r = r + [0 for i in range(len(l) - len(r))]
    return l, r

def right_order(l, r):
    if isinstance(l, int): l = [l]
    if isinstance(r, int): r = [r]
    l, r = equalize(l, r)
    
    for i in range(len(l)):
        if l[i] < r[i]:
            return True
        if l[i] > r[i]:
            return False
    return None

def check_pair(l, r):
    l = eval(l); r = eval(r)
    l, r = equalize(l, r)
    print(len(l))
    print(len(r))
    ret = None
    for i in range(len(l)):
        ret = right_order(l[i], r[i])
        if ret is not None:
            return ret

# [print(check_pair(eval(p[0]), eval(p[1]))) for p in pairs]
check_pair(pairs[6][0],pairs[6][1])



