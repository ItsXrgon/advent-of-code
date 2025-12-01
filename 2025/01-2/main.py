# Dec 1 2025 - part 2
file = open('2025/01-2/input.txt', 'r')

spins = []
for line in file:
    spins.append(line.strip())

dial: int = 50
count: int = 0
for spin in spins:
    dir = -1 if spin[0] == 'L' else 1
    offset = int(spin[1:len(spin)])
    
    old = dial
    rotation = offset % 100 # rotation overall
    loops = offset // 100 
    count += loops

    dial += rotation * dir
    if dial > 99 or (dial < 1 and old != 0):
        count += 1
    dial %= 100

print(count)