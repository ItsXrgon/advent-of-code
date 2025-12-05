# Dec 03 2025 - part 2
import time
start_time = time.perf_counter()


file = open('2025/03-2/input.txt', 'r')
banks = [line.strip() for line in file] 

total = 0

def find_next_largest(bank, start, end):
    index = start
    max = 0
    max_idx = 0
    for battery in bank[start:end]:
        index += 1
        if battery == '9':
            return battery, index
        value = int(battery)
        if value > max:
            max = value
            max_idx = index
    return str(max), max_idx

def find_largest_sum(bank, start=0, digits=12):
    if digits == 0:
        return ''

    largest, next_start = find_next_largest(bank, start, len(bank) - digits + 1)
    return largest + find_largest_sum(bank, next_start, digits-1) 

for bank in banks:
    total += int(find_largest_sum(bank, 0, 12))

print(total)

end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")