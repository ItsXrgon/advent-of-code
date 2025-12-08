# Dec 08 2025 - part 1
import time
import math
import itertools

start_time = time.perf_counter()

file = open('2025/08-1/input.txt', 'r')
boxes = []
for line in file:
    boxes.append([int(coord) for coord in line.strip().split(',')])

def get_distance(box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2

    dx = (x2 - x1) ** 2
    dy = (y2 - y1) ** 2
    dz = (z2 - z1) ** 2
    return math.sqrt(dx + dy + dz)

pair_distances = []
for pair in list(itertools.combinations(boxes, 2)):
    p1, p2 = pair
    distance = get_distance(p1, p2)
    pair_distances.append((pair, distance))

pair_distances.sort(key=lambda distance: distance[1])


def box_key(box):
    x, y, z = box
    return str(x) + ',' + str(y) + ',' + str(z)

circuits = [set([box_key(box)]) for box in boxes]

def merge_circuits(box1, box2, circuits: list[set]):
    circuit1, circuit2 = set(), set()

    box1_key = box_key(box1)
    box2_key = box_key(box2)

    for circuit in circuits:
        if box1_key in circuit:
            circuit1 = circuit
        if box2_key in circuit:
            circuit2 = circuit

    try: 
        circuits.remove(circuit1)
        circuits.remove(circuit2)
    except:
        pass
    circuits.append(circuit1.union(circuit2))
    return circuits


for i in range(1000):
    box1, box2 = pair_distances[i][0]
    merge_circuits(box1, box2, circuits)

sizes = []
for circuit in circuits:
    sizes.append(len(circuit))

sizes.sort()
sizes.reverse()
print(sizes[0] * sizes[1] * sizes[2])

end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")