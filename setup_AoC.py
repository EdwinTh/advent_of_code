import sys
import os
from pathlib import Path

# needed to get the full permission spectrum
os.umask(0)

year = sys.argv[1]
day = '0' + sys.argv[2]
day = day[-2:]

wd = os.getcwd()

folder = f"{wd}/AoC_{year}/day_{day}"
Path(folder).mkdir(parents=True, exist_ok=False)

for file in [f"data{day}.txt", f"data{day}_test.txt", f"script{day}.py"]:
    file_path = f"{folder}/{file}"
    Path(file_path).touch(mode=511, exist_ok=False)

boilerplate = f"""
with open('data{day}_test.txt') as d:
    data = [el.strip() for el in d.readlines()]
"""

with open(f"{folder}/script{day}.py", "w+") as file:
    file.write(boilerplate)