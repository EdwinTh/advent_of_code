import hashlib
with open('data04.txt') as d:
    data = [el.strip() for el in d.readlines()][0]

i = 1
while True:
    test_data = data + str(i)
    test_data = test_data.encode("utf-8")
    if hashlib.md5(test_data).hexdigest()[:5] == "0" * 5:
        break
    i += 1

print("Star 1:", i)

i = 1
while True:
    test_data = data + str(i)
    test_data = test_data.encode("utf-8")
    if hashlib.md5(test_data).hexdigest()[:6] == "0" * 6:
        break
    i += 1

print("Star 2:", i)