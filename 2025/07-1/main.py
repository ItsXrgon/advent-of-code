# Dec 07 2025 - part 1
import time

start_time = time.perf_counter()

file = open('2025/07-1/input.txt', 'r')

start = None
beam = set()
split_count = 0
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

map_height = x

def expand_beam(location: tuple):
    x, y = location

    if x == map_height:
        return 0

    if location in beam:
        return 0
    
    beam.add(location)

    next_location = (x + 1, y)

    if next_location in splitters:
        nx, ny = next_location
        left = (nx, ny+1)
        right = (nx, ny-1)

        split_count = 0
        if left not in beam:
            split_count += expand_beam(left)

        if right not in beam:
            split_count += expand_beam(right)
        return 1 + split_count
    
    return expand_beam(next_location)

print(expand_beam(start))

end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")