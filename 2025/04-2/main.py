# Dec 04 2025 - part 2
import time

start = time.perf_counter()
file = open('2025/04-2/input.txt', 'r')

rolls = set()
x = 0
for line in file:
    y = 0
    for cell in line.strip():
        if cell == '@':
            rolls.add((x,y))
        y += 1
    x += 1

def check_rolls():
    count = 0
    new_rolls = rolls.copy()
    for roll in rolls:
        x, y = roll
        adjacents = [(x+1, y+1), (x+1, y), (x+1, y-1),
                    (x, y-1), (x, y+1),
                    (x-1, y+1), (x-1, y), (x-1, y-1)]

        adjacenet_rolls = 0
        for adjacent in adjacents:
            if adjacent in rolls:
                adjacenet_rolls += 1
    
        if (adjacenet_rolls < 4):
            count += 1
            new_rolls.remove(roll)
   
    return count, new_rolls

total_count = 0
while True:
    new_count, new_rolls = check_rolls()
    if new_count == 0:
        break
    rolls = new_rolls
    total_count += new_count 

print(total_count)
end = time.perf_counter()
print(f"Took {end - start:.4f} seconds")