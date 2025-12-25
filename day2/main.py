from pathlib import Path

try:
    with open(Path(__file__).parent / 'input.txt') as f:
        inp = f.read()
except FileNotFoundError:
    print("File 'input.txt' not found! Please try again with a file present.")
    exit()

inp = [[int(y) for y in x.split('-')] for x in inp.split(',')]

invalid_count = 0
invalid_sum = 0

for range_start, range_end in inp:
    for id_to_check in range(range_start, range_end+1):
        str_id = str(id_to_check)
        l = len(str_id)
        if l % 2 != 0:
            continue
        if str_id[:l//2] == str_id[l//2:]:
            invalid_count += 1
            invalid_sum += id_to_check

print("Count:", invalid_count)
print("Sum:", invalid_sum)