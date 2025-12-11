# Dec 07 2025 - part 2
from functools import cache
import time

start_time = time.perf_counter()

file = open('2025/07-2/input.txt', 'r')

start = None
splitters = set()
x = 0
for line in file:
    y = 0
    for cell in line.strip():
        if cell == '^':
            splitters.add((x,y))
        elif cell == 'S':
            start = (x, y)
        y += 1
    x += 1

map_width = y
map_height = x

@cache
def expand_beam(location: tuple):
    x, y = location

    if x == map_height:
        return 0
    
    next_location = (x + 1, y)

    if next_location in splitters:
        nx, ny = next_location
        left = (nx, ny+1)
        right = (nx, ny-1)

        return 1 + expand_beam(left) + expand_beam(right)
    
    return expand_beam(next_location)

print(1 + expand_beam(start))

end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")