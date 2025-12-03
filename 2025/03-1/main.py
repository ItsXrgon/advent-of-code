# Dec 03 2025 - part 1
import time
start = time.perf_counter()


file = open('2025/03-1/input.txt', 'r')
banks = [line.strip() for line in file] 

total = 0

def find_next_largest(bank, start, end):
    index = start
    max = 0
    max_idx = 0
    for battery in bank[start:end]:
        index += 1
        if battery == '9':
            return (battery, index+1)
        value = int(battery)
        if value > max:
            max = value
            max_idx = index
    return str(max), max_idx

def find_largest_sum(bank, start=0, digits=2):
    if digits == 0:
        return ''

    largest, next_start = find_next_largest(bank, start, len(bank) - digits + 1)
    return largest + find_largest_sum(bank, next_start, digits-1) 

for bank in banks:
    total += int(find_largest_sum(bank, 0, 2))

print(total)

end = time.perf_counter()
print(f"Took {end - start:.4f} seconds")