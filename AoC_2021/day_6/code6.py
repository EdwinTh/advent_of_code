from collections import Counter
with open('data6.txt') as f:
    data = f.readlines()
data = [int(d) for d in data[0].split(",")]

def update_fish(data):
    new_fish_nr = len([d for d in data if d == 0])
    updated = [d-1 if d > 0 else 6 for d in data]
    return updated + [8] * new_fish_nr

star1_data = data
for i in range(80):
    star1_data = update_fish(star1_data)
print(len(star1_data))

# star 2
def update_fish2(cnt):
    new_dict = {}
    new_dict[0] = cnt.get(1, 0)
    new_dict[1] = cnt.get(2, 0)
    new_dict[2] = cnt.get(3, 0)
    new_dict[3] = cnt.get(4, 0)
    new_dict[4] = cnt.get(5, 0)
    new_dict[5] = cnt.get(6, 0)
    new_dict[6] = cnt.get(0, 0) + cnt.get(7, 0)
    new_dict[7] = cnt.get(8, 0)
    new_dict[8] = cnt.get(0, 0)
    return new_dict


star2_data = dict(Counter(data))
for i in range(256):
    star2_data = update_fish2(star2_data)

print(sum(star2_data.values()))
