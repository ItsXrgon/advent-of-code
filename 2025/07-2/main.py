# Dec 07 2025 - part 2
import time

start_time = time.perf_counter()

file = open('2025/07-2/input.txt', 'r')

start = None
splitters = set()
cache = {}
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

def expand_beam(location: tuple):
    x, y = location

    if x == map_height or y == map_height or y == -1:
        return 0
    
    next_location = (x + 1, y)

    if next_location in splitters:
        nx, ny = next_location
        left = (nx, ny+1)
        right = (nx, ny-1)

        if left not in cache:
            cache[left] =  expand_beam(left)

        if right not in cache:
            cache[right] = expand_beam(right)

        return 1 + cache[left] + cache[right]
    
    return expand_beam(next_location)

sx, sy = start
print(1 + expand_beam((sx + 1, sy)))

end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")