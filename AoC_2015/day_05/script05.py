with open('data05.txt') as d:
    data = [el.strip() for el in d.readlines()]

def three_vowel(d):
    vowels = 'aeiou'
    return sum([e in vowels for e in d]) >= 3

def two_consecutive(d):
    return any([d[i] == d[i-1] for i in range(1, len(d))])

def has_false_strings(d):
    false_strings = ['ab', 'cd', 'pq', 'xy']
    return any([fs in d for fs in false_strings])

def is_nice_string(d):
    return three_vowel(d) and two_consecutive(d) and not has_false_strings(d)

print("Star 1:", sum([is_nice_string(d) for d in data]))

def has_pairs(d):
    for i in range(len(d) -1):
        pair = d[i:i+2]
        remainder1 = d[:i]
        remainder2 = d[i+2:]
        if pair in remainder1 or pair in remainder2:
            return True
    return False

def has_aba(d):
    return any([d[i] == d[i+2] for i in range(len(d) - 2)])

def is_nice_string2(d):
    return has_pairs(d) and has_aba(d)

print("Star 2:", sum([is_nice_string2(d) for d in data]))