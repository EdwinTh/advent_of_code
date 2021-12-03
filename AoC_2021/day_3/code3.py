with open('data.txt') as f:
	data = f.readlines()
data = [d.strip() for d in data]

# star 1

def find_most_common(data, pos):
	track = {'0':0, '1':0}
	for i in data:
		track[i[pos]] += 1
	if track['0'] == track['1']:
		return 'tie'
	return '0' if track['0'] > track['1'] else '1'

def reverse_zero_one(val):
	return str(abs(int(val) - 1))
	
most_common = []
for i in range(len(data[0])):
	most_common.append(find_most_common(data, i))

gamma_bin = ''.join(most_common)

epsilon_bin = ''.join([reverse_zero_one(i) for i in most_common])

print(int(gamma_bin, 2) * int(epsilon_bin, 2))

# star 2

def keep_only(data, pos, value):
	return [d for d in data if d[pos] == value]

oxygen_vals = []
oxygen_data = data

for i in range(len(oxygen_data[0])):
	oxygen_vals.append(find_most_common(oxygen_data, i))
	if oxygen_vals[i] == 'tie':
		oxygen_vals[i] = '1'
	oxygen_data = keep_only(oxygen_data, i, oxygen_vals[i])
	if len(oxygen_data) == 1:
		break

co2_vals = []
co2_data = data

for i in range(len(co2_data[0])):
	co2_vals.append(find_most_common(co2_data, i))
	if co2_vals[i] == 'tie':
		co2_vals[i] = '0' 
	else:
		co2_vals[i] = reverse_zero_one(co2_vals[i])
	co2_data = keep_only(co2_data, i, co2_vals[i])
	if len(co2_data) == 1:
		break

print(int(''.join(oxygen_data), 2) * int(''.join(co2_data), 2))