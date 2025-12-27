from pathlib import Path
import time

start_time = time.perf_counter()

try:
    with open(Path(__file__).parent / 'input.txt') as f:
        inp = f.read().split()
except FileNotFoundError:
    print("File 'input.txt' not found! Please try again with a file present.")
    exit()

dial_position = 50
passcode = 0

for instruction in inp:
    direction = instruction[0]
    turns = int(instruction[1:])
    
    # Turn negative if direction is left.
    negative = direction == 'L'
    
    for _ in range(turns):
        dial_position += -1 if negative else 1
        dial_position %= 100

        # If dial position is 0, increment the passcode
        if dial_position == 0:
            passcode += 1

end_time = time.perf_counter()

print("Time taken:", end_time - start_time)
print("Final dial position:", dial_position)
print("Passcode:", passcode)