# Dec 06 2025 - part 1
import time

start_time = time.perf_counter()

file = open('2025/06-1/input.txt', 'r')
row1, row2, row3, row4, row5 = [line.strip().split() for line in file]

result = 0
for i in range(len(row1)):
    symbol = row5[i]
    r1 = int(row1[i])
    r2 = int(row2[i])
    r3 = int(row3[i])
    r4 = int(row4[i])
    if symbol == '*':
        result += r1 * r2 * r3 * r4
    else:
        result += r1 + r2 + r3 + r4

print(result)


end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")