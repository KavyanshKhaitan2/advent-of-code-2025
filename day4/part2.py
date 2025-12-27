from pathlib import Path
import time



try:
    with open(Path(__file__).parent / "input.txt") as f:
        inp = f.read()
except FileNotFoundError:
    print("File 'input.txt' not found! Please try again with a file present.")
    exit()

inp = inp.splitlines()
inp = [[col == "@" for col in row] for row in inp]


def iterate(inp:list[list]):
    new_inp = [x.copy() for x in inp]
    accessible_rolls = 0
    for y, row in enumerate(inp):
        for x, col in enumerate(row):
            if not col and not verbose:
                continue
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
                new_inp[y][x] = False
            else:
                if verbose:
                    print("@" if col else ".", end="", flush=True)
        if verbose:
            print()
    return accessible_rolls, new_inp


start_time = time.perf_counter()

accessible_rolls = 0
iteration_count = 0

# Disable printing!
verbose = False

while True:
    more_accessible_rolls, new_inp = iterate(inp)

    if more_accessible_rolls == 0:
        break
    
    print(f"Accessed {more_accessible_rolls} rolls.")
    
    accessible_rolls += more_accessible_rolls
    inp = new_inp
    iteration_count += 1

end_time = time.perf_counter()

print("Time taken:", end_time - start_time)
print("Iterations required:", iteration_count)
print("Accessible rolls:", accessible_rolls)
