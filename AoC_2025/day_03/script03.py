with open('data03.txt') as d:
    data = [el.strip() for el in d.readlines()]
    data = [[digit for digit in el] for el in data]

def find_max_digit_i(digits, i_start=0):
    max_d = "0"
    max_i = i_start
    for i,d in enumerate(digits):
        if d > max_d:
            max_d = d
            max_i = i + i_start
    return max_i

def find_joltage(digits):
    digit_i1 = find_max_digit_i(digits[:-1])
    digit_i2 = find_max_digit_i(digits[digit_i1+1:], digit_i1+1)
    return int(digits[digit_i1] + digits[digit_i2])

print("Star 1:", sum([find_joltage(digits) for digits in data]))

def find_joltage_2(digits, switched_on=12):
    digits_i = []
    for i in range(switched_on, 0, -1):
        start_val = 0 if len(digits_i) == 0 else digits_i[-1]+1
        digits_selection = digits[start_val:] if i == 1 else digits[start_val:-(i-1)]
        digits_i.append(find_max_digit_i(digits_selection, start_val))
    joltage = ''
    for i in digits_i:
        joltage += digits[i]
    return int(joltage)

print("Star 2:", sum([find_joltage_2(digits) for digits in data]))
