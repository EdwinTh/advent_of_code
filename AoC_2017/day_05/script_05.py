with open("data05.txt") as d:
    data = d.readlines()
data = [int(d.strip()) for d in data]
cnt = 0
ind = 0
while ind in range(len(data)):
    jump = data[ind]
    data[ind] += 1
    ind += jump
    cnt += 1
print("star 1: " + str(cnt))

with open("data05.txt") as d:
    data = d.readlines()
data = [int(d.strip()) for d in data]
cnt = 0
ind = 0
while ind in range(len(data)):
    jump = data[ind]
    if jump > 2:
        data[ind] -= 1
    else:
        data[ind] += 1
    ind += jump
    cnt += 1
print("star 2: " + str(cnt))