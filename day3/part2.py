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


total_joltage = 0

for bank in inp:
    digits = []
    first_digit = max([int(x) for x in bank[0:-1]])
    second_digit = max([int(x) for x in bank[bank.index(str(first_digit)) + 1 :]])
    
    search_string = bank
    
    for i in range(12, 1, -1):
        # print("SS:", search_string)
        digit = max([int(x) for x in search_string[:-i+1]])
        search_string = search_string[search_string.find(str(digit))+1:]
        digits.append(digit)
    
    digits.append(max([int(x) for x in search_string])) # Special treatment for last digit
    
    joltage = int(''.join([str(x) for x in digits]))
    total_joltage += joltage
    # print("Jo:",joltage)

end_time = time.perf_counter()

print("Time taken:", end_time - start_time)
print("Total joltage:", total_joltage)
