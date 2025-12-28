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

split_count = 0

beam_positions = {inp[0].find("S")}
for i, line in enumerate(inp):
    to_add = set()
    to_remove = set()
    for beam_position in beam_positions:
        if line[beam_position] == "^":
            to_remove.add(beam_position)
            to_add.add(beam_position - 1)
            to_add.add(beam_position + 1)
            split_count += 1
    beam_positions.difference_update(to_remove)
    beam_positions.update(to_add)

print(beam_positions)

end_time = time.perf_counter()
print("Time taken:", end_time - start_time)
print("Grand total:", split_count)
