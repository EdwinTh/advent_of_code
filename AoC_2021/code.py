with open('data.txt') as f:
	data = f.readlines()

def find_most_common(data, pos):
	track = {'0':0, '1':0}
	for i in data:
		track[i[pos]] += 1
	print(track)

find_most_common(data, 0)