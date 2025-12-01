with open('data01.txt') as d:
    data = [el.strip() for el in d.readlines()]
    # strip off the hundreds, they don't do anything for star 1
    data = [{'dir':d[:1], 'val':int(d[1:][-2:])} for d in data]

zero_counter = 0
place = 50

for d in data:
    place += -1*d['val'] if d['dir'] == 'L' else d['val']
    if place < 0:
        place = 100 + place
    if place > 99:
        place = place - 100
    zero_counter += place == 0

print('Star 1 =', zero_counter)

with open('data01.txt') as d:
    data = [el.strip() for el in d.readlines()]
    data = [{'dir':d[:1], 'val':int(d[1:])} for d in data]

new_data = []
for d in data:
    if d['val'] > 100:
        new_data += [{'dir':d['dir'], 
                      'val':int(str(d['val'])[-2:]), 
                      'hundreds':d['val'] // 100}]
    else:
        new_data += [{'dir':d['dir'], 'val':d['val'], 'hundreds':0}]

zero_counter = 0
prev_place = place = 50

for nr,d in enumerate(new_data):
    zero_counter += d['hundreds']
    place += -1*d['val'] if d['dir'] == 'L' else d['val']
    print(d)
    print('place before', place)
    if place == 0:
        zero_counter += 1
    elif place < 0:
        # if this is not true the previous was 0 and we did not pass 0 in this run
        if place != d['val']*-1:
            zero_counter += 1
        place = 100 + place
    elif place > 99:
        zero_counter += 1
        place = place - 100
    
    print('place after', place)
    print(zero_counter)

print('Star 2 =', zero_counter)
