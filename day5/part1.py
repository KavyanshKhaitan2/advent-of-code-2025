from pathlib import Path
import time


start_time = time.perf_counter()

try:
    with open(Path(__file__).parent / "input.txt") as f:
        inp = f.read()
except FileNotFoundError:
    print("File 'input.txt' not found! Please try again with a file present.")
    exit()

fresh_ranges, available_ids = inp.split('\n\n')
fresh_ranges = [[int(y) for y in x.split('-')] for x in fresh_ranges.split('\n')]
available_ids = [int(x) for x in available_ids.split('\n')]

fresh_count = 0

# Disable printing!
verbose = False

for available_id in available_ids:
    for start, end in fresh_ranges:
        if available_id in range(start, end+1):
            fresh_count += 1
            break


end_time = time.perf_counter()

print("Time taken:", end_time - start_time)
print("Fresh count:", fresh_count)
