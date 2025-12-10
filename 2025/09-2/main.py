# Dec 09 2025 - part 2
import time
import itertools

start_time = time.perf_counter()

file = open('2025/09-2/input.txt', 'r')
tiles = []
for line in file:
    x, y = [int(num) for num in line.strip().split(',')]
    tiles.append((x, y))

def get_size(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2

    dx = abs(x2 - x1) + 1
    dy = abs(y2 - y1) + 1
    return dx * dy

def valid_combination(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    
    rect_lower_x = min(x1, x2)
    rect_upper_x = max(x1, x2)
    rect_lower_y = min(y1, y2)
    rect_upper_y = max(y1, y2)

    if x1 == x2 or y1 == y2:
        return True

    for start, end in itertools.pairwise(tiles + [tiles[0]]):
        sx, sy = start
        ex, ey = end

        edge_lower_x = min(sx, ex)
        edge_upper_x = max(sx, ex)
        edge_lower_y = min(sy, ey)
        edge_upper_y = max(sy, ey)

        if not (
            edge_upper_x <= rect_lower_x or rect_upper_x <= edge_lower_x or
            edge_upper_y <= rect_lower_y or rect_upper_y <= edge_lower_y
        ):
            return False

    return True


combinations = [combination for combination in list(itertools.combinations(tiles, 2)) if valid_combination(*combination)]
rectangles = []
for pair in combinations:
    t1, t2 = pair
    size = get_size(t1, t2)
    rectangles.append((pair, size))

rectangles.sort(key=lambda size: size[1], reverse=True)
print(rectangles[0][1])
end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")