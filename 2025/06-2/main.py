# Dec 06 2025 - part 2
import time

start_time = time.perf_counter()

file = open('2025/06-2/input.txt', 'r')
row1, row2, row3, row4, symbols = [line for line in file]

symbols = symbols.split()

def parse_rows(row1, row2, row3, row4):
    cols = []
    nums = []
    for i in range(len(row1)):
        r1 = row1[i]
        r2 = row2[i]
        r3 = row3[i]
        r4 = row4[i]
        if (r1 == ' ' and r2 == ' ' and r3 == ' ' and r4 == ' ') or i == len(row1) - 1:
            cols.append(nums)
            nums = []
            continue
        nums.append(r1.strip() + r2.strip() + r3.strip() + r4.strip())
    return cols

cols = parse_rows(row1, row2, row3, row4)

result = 0
for i in range(len(cols)):
    symbol = symbols[i]
    nums = [int(num) for num in cols[i]]
    if symbol == '*':
        total = 1
        for num in nums:
            total *= num
    else:
        total = 0
        for num in nums:
            total += num
    result += total
print(result)


end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")