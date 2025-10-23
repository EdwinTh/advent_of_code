from itertools import product
with open('data07.txt') as d:
    data = [el.strip() for el in d.readlines()]

class Evaluation:
    def __init__(self, data):
        self.test_value = int(data.split(':')[0])
        self.values = [int(v) for v in data.split(':')[1].strip().split(" ")]
        self.n = len(self.values)

    def _get_all_operators(self):
        self.operators = product('+*', repeat = self.n - 1)

    def _eval_operator(self, operator):
        value = 0
        operator = ['+'] + [o for o in operator] 
        for i in range(self.n):
            if operator[i] == '+':
                value += self.values[i]
            else:
                value *= self.values[i]
        return value

    def return_value(self):
        for operator in self.operators:
            if self._eval_operator(operator) == self.test_value:
                return self.test_value
        return 0

    def evaluate(self):
        self._get_all_operators()
        return self.return_value()

print("Star 1:", sum([Evaluation(d).evaluate() for d in data]))

class Evaluation2:
    def __init__(self, data):
        self.test_value = int(data.split(':')[0])
        self.values = [int(v) for v in data.split(':')[1].strip().split(" ")]
        self.n = len(self.values)

    def _get_all_operators(self):
        self.operators = product('+*|', repeat = self.n - 1)

    def _eval_operator(self, operator):
        value = 0
        operator = ['+'] + [o for o in operator] 
        for i in range(self.n):
            if operator[i] == '+':
                value += self.values[i]
            elif operator[i] == '*':
                value *= self.values[i]
            else:
                value = int(str(value) + str(self.values[i]))
        return value

    def return_value(self):
        for operator in self.operators:
            if self._eval_operator(operator) == self.test_value:
                return self.test_value
        return 0

    def evaluate(self):
        self._get_all_operators()
        return self.return_value()

print("Star 2:", sum([Evaluation2(d).evaluate() for d in data]))
