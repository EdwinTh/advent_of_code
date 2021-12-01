# star 1
with open('data.txt', 'r') as f:
	nrs = f.readlines()

nrs = [int(l) for l in nrs]
next_larger = [next for prev, next in zip(nrs[:-1], nrs[1:]) if next > prev]

print(len(next_larger))

# start 2
sums = [a + b + c for a,b,c in zip(nrs[:-2], nrs[1:-1], nrs[2:])]
next_larger_sums = [next for prev, next in zip(sums[:-1], sums[1:]) if next > prev]

print(len(next_larger_sums))