with open("data02.txt") as d:
    data = [el.strip() for el in d.readlines()]

points = {
    "A Y": 2 + 6,
    "A X": 1 + 3,
    "A Z": 3 + 0,
    "B Y": 2 + 3,
    "B X": 1 + 0,
    "B Z": 3 + 6,
    "C Y": 2 + 0,
    "C X": 1 + 6,
    "C Z": 3 + 3
}

print("Star 1 =", str(sum([points[el] for el in data])))

points2 = {
    "A Y": 3 + 1,
    "A X": 0 + 3,
    "A Z": 6 + 2,
    "B Y": 3 + 2,
    "B X": 0 + 1,
    "B Z": 6 + 3,
    "C Y": 3 + 3,
    "C X": 0 + 2,
    "C Z": 6 + 1
}
print("Star 2 =", str(sum([points2[el] for el in data])))