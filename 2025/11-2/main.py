# Dec 11 2025 - part 2
from functools import cache
import time

start_time = time.perf_counter()

file = open('2025/11-2/input.txt', 'r')
devices = {}
start = ()
for line in file:
    row = line.replace(':', '').strip().split(' ')
    input = row[0]
    outputs = set(row[1::])
    
    devices[input] = outputs

@cache
def expand(input, dac: bool, ftt: bool):
    paths = 0
    outputs = devices[input]

    ftt |= input == 'fft'
    dac |= input == 'dac'

    for output in outputs:
        if output == 'out':
            if dac and ftt:
                paths += 1
            continue
        paths += expand(output, dac, ftt)

    return paths

print(expand('svr', False, False))


end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")