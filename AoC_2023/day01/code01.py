import re
with open('data01.txt') as d:
    data = [el.strip() for el in d.readlines()]

nrs = [re.findall('\d', d) for d in data]
# first_last_int = [int(n[0] + n[-1]) for n in nrs]
# print("Star 1: ", str(sum(first_last_int)))

three_letter = {"one":'1', "two":"2", "six":"6"}
four_letter = {"four":"4", "five":"5", "nine":"9"}
five_letter = {"three":"3", "seven":"7", "eight":"8"}
nrs_list = [str(nr) for nr in range(1,10)]

def return_nr(str_val, lookup):
    if str_val in lookup:
        return lookup[str_val]

def collect_all_nrs(strval):
    nrs = []
    for i in range(len(strval)):
        nr =  strval[i] if strval[i] in nrs_list else None
        three = return_nr(strval[i:min(len(strval),i+3)], three_letter)
        four = return_nr(strval[i:min(len(strval),i+4)], four_letter)
        five = return_nr(strval[i:min(len(strval),i+5)], five_letter)
        if nr is not None: nrs.append(nr)
        if three is not None: nrs.append(three)
        if four is not None: nrs.append(four)
        if five is not None: nrs.append(five)
    return nrs

data2 = [collect_all_nrs(d) for d in data]

print(data[-10:])
print(data2[-10:])
first_last_int2 = [int(n[0] + n[-1]) for n in data2]
print("Star 2: ", str(sum(first_last_int2)))

