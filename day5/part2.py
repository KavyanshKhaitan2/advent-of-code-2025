from pathlib import Path
import time


start_time = time.perf_counter()

try:
    with open(Path(__file__).parent / "input.txt") as f:
        inp = f.read()
except FileNotFoundError:
    print("File 'input.txt' not found! Please try again with a file present.")
    exit()

fresh_ranges, _ = inp.split("\n\n")
fresh_ranges = [[int(y) for y in x.split("-")] for x in fresh_ranges.split("\n")]
fresh_ranges = sorted(fresh_ranges, key=lambda x: x[1])

def merge_ranges(fresh_ranges):
    added = False
    new_ranges = []
    for i, (start, end) in enumerate(fresh_ranges):
        if added:
            added = False
            continue
        try:
            next_start, next_end = fresh_ranges[i+1]
        except IndexError:
            new_ranges.append([start, end])
            continue
        if end >= next_start:
            added = True
            new_ranges.append([min(start, next_start), max(end, next_end)])
        else:
            added = False
            new_ranges.append([start, end])
    return sorted(new_ranges)



fresh_count = 0
print(len(fresh_ranges))
while True:
    old_len = len(fresh_ranges)
    fresh_ranges = merge_ranges(fresh_ranges)
    print(len(fresh_ranges))
    if old_len == len(fresh_ranges):
        break

for start, end in fresh_ranges:
    fresh_count += end - start + 1

end_time = time.perf_counter()

print("Time taken:", end_time - start_time)
print("Fresh count:", fresh_count)
