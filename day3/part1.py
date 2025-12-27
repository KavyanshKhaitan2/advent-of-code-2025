from pathlib import Path
import time


start_time = time.perf_counter()

try:
    with open(Path(__file__).parent / 'input.txt') as f:
        inp = f.read()
except FileNotFoundError:
    print("File 'input.txt' not found! Please try again with a file present.")
    exit()

inp = inp.splitlines()


total_joltage = 0

for bank in inp:
    first_digit = max([int(x) for x in bank[0:-1]])
    second_digit = max([int(x) for x in bank[bank.index(str(first_digit))+1:]])
    joltage = int(f"{first_digit}{second_digit}")
    total_joltage += joltage

end_time = time.perf_counter()

print("Time taken:", end_time - start_time)
print("Total joltage:", total_joltage)