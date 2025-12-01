# Dec 1 2025 - part 1 
file = open('2025/01-1/input.txt', 'r')

spins = []
for line in file:
    spins.append(line.strip())

dial: int = 50
count: int = 0
for spin in spins:
    dir = -1 if spin[0] == 'L' else 1
    offset = int(spin[1:len(spin)])
    
    signed_offset =  offset * dir
    dial += offset
    dial %= 100
    
    if dial == 0:
        count += 1
print(count)