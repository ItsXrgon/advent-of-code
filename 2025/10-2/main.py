from scipy.optimize import linprog


a = b = 0
for _, *buttons, joltage in map(str.split, open('2025/10-2/input.txt')):
    buttons = [eval(b[:-1]+',)') for b in buttons]
    joltage = eval(joltage[1:-1])
    numbers = range(len(joltage))

    c = [1 for _ in buttons]
    A = [[i in b for b in buttons] for i in numbers]

    b += linprog(c, A_eq=A, b_eq=joltage, integrality=1).fun

print(int(b))