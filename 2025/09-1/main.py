# Dec 09 2025 - part 1
import time
import itertools

start_time = time.perf_counter()

file = open('2025/09-1/input.txt', 'r')
tiles = []
for line in file:
    tiles.append([int(num) for num in line.strip().split(',')])

def get_size(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2

    dx = abs(x2 - x1) + 1
    dy = abs(y2 - y1) + 1
    return dx * dy

rectangles = []
for pair in list(itertools.combinations(tiles, 2)):
    t1, t2 = pair
    size = get_size(t1, t2)
    rectangles.append((pair, size))

rectangles.sort(key=lambda size: size[1], reverse=True)
print(rectangles[0][1])

end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")