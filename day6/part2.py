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

inp = inp.splitlines()
num_count = len(inp) - 1
grand_total = 0

op_line = inp[num_count]

for i, op in enumerate(op_line):
    if op == ' ':
        continue
    for j, next_op in enumerate(op_line[i:]):
        if len(op_line[i:]) - 1 == j:
            j += 1
        if j == 0:
            continue
        if next_op == ' ':
            continue
        j -= 1
        break
    start, end = i, i+j
    block = []
    for j in range(num_count):
        x = inp[j][start:end]
        block.append(x)

    block_result = 0 if op == '+' else 1
    
    for j in range(len(block[0])):
        num = ''.join([k[j] for k in block])
        num = int(num)
        if op == '+':
            block_result += num
        if op == '*':
            block_result *= num
    grand_total += block_result



end_time = time.perf_counter()

print("Time taken:", end_time - start_time)
print("Grand total:", grand_total)
