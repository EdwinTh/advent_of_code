# star 1
with open('data.txt') as f:
	data = f.readlines()
data = [d.strip() for d in data]


def find_most_common(data, pos):
	track = {'0':0, '1':0}
	for i in data:
		track[i[pos]] += 1
	return '0' if track['0'] > track['1'] else '1'
	
most_common = []
for i in range(len(data[0])):
	most_common.append(find_most_common(data, i))

gamma_bin = ''.join(most_common)

epsilon_bin = ''.join([str(abs(int(i)-1)) for i in most_common])

print(int(gamma_bin, 2) * int(epsilon_bin, 2))