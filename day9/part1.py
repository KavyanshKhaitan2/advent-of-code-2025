from pathlib import Path
import time

start_time = time.perf_counter()

try:
    with open(Path(__file__).parent / "input.txt") as f:
        inp = f.read()
except FileNotFoundError:
    print("File 'input.txt' not found! Please try again with a file present.")
    exit()

inp = inp.splitlines()
inp = [[int(y) for y in x.split(',')] for x in inp]

largest_area = 0
start, end = (0, 0), (0, 0)

for x1, y1 in inp:
    for x2, y2 in inp:
        if x1 == x2 and y1 == y2:
            continue
        current_area = abs(x2-x1+1) * abs(y2-y1+1)
        if current_area > largest_area:
            largest_area = current_area
            start = x1, y1
            end = x2, y2

end_time = time.perf_counter()
print("Time taken:", end_time - start_time)
print("Largest area:", largest_area)
print("Coords:", start, end)
