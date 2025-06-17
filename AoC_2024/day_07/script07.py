from itertools import combinations_with_replacement, permutations
with open('data07_test.txt') as d:
    data = [el.strip() for el in d.readlines()]

class Combination:
    def __init__(self, data):
        self.test_value = int(data.split(':')[0])
        self.values = [int(v) for v in data.split(':')[1].strip().split(" ")]

    def _get_all_operators(self):
        len(self.values)
