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
inp = [[col == "@" for col in row] for row in inp]

accessible_rolls = 0

# Disable printing!
verbose = False

for y, row in enumerate(inp):
    for x, col in enumerate(row):
        adj_rolls = []
        adj_roll_coords_set = [
            (y - 1, x - 1),
            (y - 1, x),
            (y - 1, x + 1),
            (y, x - 1),
            (y, x + 1),
            (y + 1, x - 1),
            (y + 1, x),
            (y + 1, x + 1),
        ]
        for coords in adj_roll_coords_set:
            row = {i: m for i, m in enumerate(inp)}.get(coords[0], [False] * 3)
            adj_rolls.append({i: m for i, m in enumerate(row)}.get(coords[1], False))

        if sum(adj_rolls) < 4 and col:
            if verbose:
                print("x", end="", flush=True)
            accessible_rolls += 1
        else:
            if verbose:
                print("@" if col else ".", end="", flush=True)
    if verbose:
        print()


end_time = time.perf_counter()

print("Time taken:", end_time - start_time)
print("Accessible rolls:", accessible_rolls)
