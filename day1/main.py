from pathlib import Path

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
    
    # Make turns negative if direction is 'L'
    if direction == 'L':
        turns = -turns
    
    dial_position += turns # Change the direction of the dial according to number of turns.
    dial_position %= 100 # The dial can roll over (in both directions), mod is a mathematical way of doing it.

    # If dial position is 0, increment the passcode
    if dial_position == 0:
        passcode += 1

print("Final dial position:", dial_position)
print("Passcode:", passcode)