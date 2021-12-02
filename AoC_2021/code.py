with open('data.txt') as f:
	data = f.readlines()

print([el.split(' ') for el in data])
print('jos')