# Dec 2 2025 - part 1 
file = open('2025/02-1/input.txt', 'r')

ranges: list[tuple] = []
for line in file:
    raw_ranges = line.split(',')
    for raw_range in raw_ranges:
        start, end = raw_range.split('-')
        ranges.append([int(start), int(end)])

result: int = 0
for start, end in ranges:
    for n in range(start, end+1):
        num = str(n)
        length = len(num)
        if length % 2 == 1:
            continue
        left = num[0:length//2]
        right = num[length//2:length]
        if left == right:
            result += n
print(result)
