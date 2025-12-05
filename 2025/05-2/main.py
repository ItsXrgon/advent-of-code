# Dec 05 2025 - part 2
import time

start_time = time.perf_counter()

fresh_ranges: list = []

with open('2025/05-2/input.txt', 'r') as f:
    id_ranges, _ = f.read().split('\n\n')
    for id_range in id_ranges.split('\n'):
        start, end = [int(num) for num in id_range.split('-')]
        fresh_ranges.append([start, end])

fresh_ranges.sort(key=lambda interval: interval[0])
merged_ranges = [fresh_ranges[0]]
for current in fresh_ranges:
    previous = merged_ranges[-1]
    if current[0] <= previous[1]:
        previous[1] = max(previous[1], current[1])
    else:
        merged_ranges.append(current)
    
count = 0
for range in merged_ranges:
    s1, e1 = range
    count += e1 - s1 + 1

print(count)
end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")

# > 302210835438280 
# < 391261757565058
# < 354363325825916