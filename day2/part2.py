# NOT COMPLETELY FUNCTIONAL
# I dont know why tho.

from pathlib import Path

try:
    with open(Path(__file__).parent / "input.txt") as f:
        inp = f.read()
except FileNotFoundError:
    print("File 'input.txt' not found! Please try again with a file present.")
    exit()

inp = [[int(y) for y in x.split("-")] for x in inp.split(",")]

invalid_count = 0
invalid_sum = 0

for range_start, range_end in inp:
    for id_to_check in range(range_start, range_end + 1):
        str_id = str(id_to_check)
        length = len(str_id)
        
        invalid = False
        
        if str_id[: length // 2] == str_id[length // 2 :]:
            invalid = True

        if all([x == str_id[0] for x in str_id]):
            invalid = True
        
        for i in range(2, length):
            if invalid:
                break
            if length % i != 0:
                continue
            length_of_parts = length // i
            parts = []
            current_part = ""
            invalid_till_here = True
            for c in str_id:
                current_part += c
                if len(current_part) == length_of_parts:
                    parts.append(current_part)
                    if current_part != parts[0]:
                        invalid_till_here = False
                        break
                    current_part = ""
            if invalid_till_here:
                invalid = True
                break
        if invalid:
            invalid_count += 1
            invalid_sum += id_to_check

print("Count:", invalid_count)
print("Sum:", invalid_sum)
