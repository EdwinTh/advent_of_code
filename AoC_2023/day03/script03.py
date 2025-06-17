with open('data03.txt') as d:
    data = [el.strip() for el in d.readlines()]

symbol_positions = []
nrs = []
nr_start = []
next_nr = ""
asterisk_positions = []

def create_adjacent_list(s, e):
    adjacent = [[s[0],s[1]-1], [e[0], e[1]+1]]
    lower = [[s[0]-1, c] for c in range(s[1]-1, e[1]+2)]
    higher = [[s[0]+1, c] for c in range(s[1]-1, e[1]+2)]
    return adjacent + lower + higher

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] in [str(el) for el in list(range(10))]:
            if nr_start == []:
                nr_start = [i,j]
            next_nr += data[i][j]
            last_ind = [i,j]
        else:
            if next_nr != "":
                nrs.append([next_nr, create_adjacent_list(nr_start, last_ind)])
                next_nr = ""
                nr_start = []        
            if data[i][j] != ".":
                symbol_positions.append([i,j])
            if data[i][j] == "*":
                asterisk_positions.append([i,j])
            

def return_if_symbol_adjacent(nr):
    for s in symbol_positions:
        if s in nr[1]:
            return nr[0]
    return "0"

print("Star 1:", sum([int(return_if_symbol_adjacent(nr)) for nr in nrs]))

def return_prod_if_two_nrs_adacent(apos):
    nr1 = nr2 = ""
    for nr in nrs:
        if apos in nr[1]:
            if nr1 == "":
                nr1 = nr[0]
            else:
                nr2 = nr[0]
    if nr2 != "":
        return int(nr1) * int(nr2)
    else:
        return 0

print("Star 2:", sum([return_prod_if_two_nrs_adacent(apos) for apos in asterisk_positions])) 
