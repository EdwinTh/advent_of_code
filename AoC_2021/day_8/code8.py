from collections import Counter
with open('test_data8.txt') as f:
    data = f.readlines()

# star 1
second_part = [d.split('|')[1].strip() for d in data]
cnt = Counter([len(el) for s in second_part for el in s.split(' ')])
print(cnt[2] + cnt[3] + cnt[4] + cnt[7])

# star 2


