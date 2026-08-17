from math import sqrt, prod
from collections import Counter
with open('data08.txt') as d:
    data = [el.strip().split(',') for el in d.readlines()]
    data = [[int(el) for el in d] for d in data]

CONNECTIONS = 10 if len(data) == 20 else 1000

def get_dist(el1, el2):
    return sqrt(sum([(el1[0]-el2[0])**2, (el1[1]-el2[1])**2, (el1[2]-el2[2])**2]))

def create_sorted_distances(data):
    distances = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i >= j:
                continue
            distances.append([data[i], data[j], get_dist(data[i], data[j])])
    return sorted(distances, key = lambda x:x[-1])

class Circuits:

    def __init__(self, data):
        self.circuits = [[d] for d in data]
        self.distances = create_sorted_distances(data)
        self.last_merged = []

    def _merge_closest_distance(self):
        closest = self.distances[0]
        ind1 = [i for i,c in enumerate(self.circuits) if closest[0] in c][0]
        ind2 = [i for i,c in enumerate(self.circuits) if closest[1] in c][0]
        self.last_merged = [closest[0], closest[1]]
        new_circuit = self.circuits[ind1] + self.circuits[ind2]
        new_circuit_dedup = [x for i,x in enumerate(new_circuit) if x not in new_circuit[:i]]
        circuits_merged_removed = [el for i,el in enumerate(self.circuits) if i not in [ind1, ind2]]
        self.circuits = circuits_merged_removed + [new_circuit_dedup]
        self.distances = self.distances[1:]

    def do_x_merges(self, x):
        for i in range(x):
            self._merge_closest_distance()

    def get_n_largest_circuits(self, n):
        lengths = sorted([len(x) for x in self.circuits])
        return lengths[-n:]

    def merge_to_one_circuit(self):
        while len(self.circuits) > 1:
            self._merge_closest_distance()

c = Circuits(data)
c.do_x_merges(CONNECTIONS)
print("Star 1:", str(prod(c.get_n_largest_circuits(3))))

c.merge_to_one_circuit()
print("Star 2:", str(c.last_merged[0][0] * c.last_merged[1][0]))