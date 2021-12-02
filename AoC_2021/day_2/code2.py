# star 1
with open('data.txt') as f:
	data = f.readlines()

splitted = [el.split(' ') for el in data]

pos = {'horizontal': 0, 'depth' : 0}

for i in splitted:
	if i[0] == 'forward':
		pos['horizontal'] = pos['horizontal'] + int(i[1])
	elif i[0] == 'down':
		pos['depth'] = pos['depth'] + int(i[1])
	elif i[0] == 'up':
		pos['depth'] = pos['depth'] - int(i[1])

print(pos['horizontal'] * pos['depth'])

# star 2
pos = {'horizontal': 0, 'depth' : 0, 'aim' : 0}

for i in splitted:
	if i[0] == 'forward':
		pos['horizontal'] = pos['horizontal'] + int(i[1])
		pos['depth'] = pos['depth'] + int(i[1]) * pos['aim']
	elif i[0] == 'down':
		pos['aim'] = pos['aim'] + int(i[1])
	elif i[0] == 'up':
		pos['aim'] = pos['aim'] - int(i[1])

print(pos['horizontal'] * pos['depth'])