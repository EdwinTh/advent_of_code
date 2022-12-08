with open("data06.txt") as d:
    data = d.read()

for i in range(4,len(data)):
    if len(set(data[i-4:i])) == 4:
        print("Star 1 =", i)
        break

for i in range(14,len(data)):
    if len(set(data[i-14:i])) == 14:
        print("Star 2 =", i)
        break