with open("data01.txt") as d:
    data = d.read()

accumelater = 0
for i in range(1, len(data)):
    if data[i-1] == data[i]:
        accumelater += int(data[i])
if data[0] == data[-1]:
    accumelater += int(data[0])
print("Value for star 1 is " + str(accumelater))

accumelater = 0
for i in range(0, len(data)):
    match_ind = i + (len(data) // 2)
    if match_ind >= len(data):
        match_ind = match_ind - len(data)
    if data[i] == data[match_ind]:
        accumelater += int(data[i])
print("Value for star 2 is " + str(accumelater))