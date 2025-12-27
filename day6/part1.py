from pathlib import Path
import time
from functools import reduce

def product(iterable):
    return reduce(lambda x, y: x*y, iterable)

start_time = time.perf_counter()

try:
    with open(Path(__file__).parent / "input.txt") as f:
        inp = f.read()
except FileNotFoundError:
    print("File 'input.txt' not found! Please try again with a file present.")
    exit()

inp = [x.split() for x in inp.splitlines()]
num_count = len(inp) - 1
grand_total = 0

for i, _ in enumerate(inp[0]):
    nums = [int(inp[x][i]) for x in range(num_count)]
    op = inp[4][i]
    if op == '+':
        grand_total += sum(nums)
    elif op == '*':
        grand_total += product(nums)
    else:
        print(f"ERROR: Operator '{op}' not found.")


end_time = time.perf_counter()

print("Time taken:", end_time - start_time)
print("Grand total:", grand_total)
