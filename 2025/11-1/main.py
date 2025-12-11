# Dec 11 2025 - part 1
from functools import cache
import time

start_time = time.perf_counter()

file = open('2025/11-1/input.txt', 'r')
devices = {}
for line in file:
    row = line.replace(':', '').strip().split(' ')
    devices[row[0]] = set(row[1::])

@cache
def expand(input):
    paths = 0
    outputs = devices[input]
    for output in outputs:
        if output == 'out':
            paths += 1
        else:
            paths += expand(output)

    return paths

print(expand('you'))


end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")