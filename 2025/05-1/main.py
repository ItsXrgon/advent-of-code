# Dec 05 2025 - part 1
import time

start_time = time.perf_counter()

fresh_ranges: list[tuple] = []
ingredients: set[int] = []

with open('2025/05-1/input.txt', 'r') as f:
    id_ranges, ingredients_list = f.read().split('\n\n')
    ingredients = set([int(ingredient) for ingredient in ingredients_list.split('\n')])
    for id_range in id_ranges.split('\n'):
        start, end = [int(num) for num in id_range.split('-')]
        fresh_ranges.append((start, end))

count = 0
for ingredient in ingredients:
    for start, end in fresh_ranges:
        if ingredient >= start and ingredient <= end:
            count +=1
            break

print(count)


end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")