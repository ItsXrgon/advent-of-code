# Dec 10 2025 - part 1
import re
import time

start_time = time.perf_counter()

file = open('2025/10-1/input.txt', 'r')

rows = []
for line in file:
    target = re.findall(r"\[.*?\]", line)[0].replace("[", '').replace("]", '')
    buttons = [buttons.replace("(", '').replace(")", '').split(',') for buttons in re.findall(r"\(.*?\)", line)]
    voltages = re.findall(r"\{.*?\}", line)[0].replace("{", '').replace("}", '').split(',')
    rows.append((target, buttons, voltages))

def apply_button(diagram, button):
    updated_diagram = [d for d in diagram]
    for b in button:
        idx = int(b)
        updated_diagram[idx] = '.' if diagram[idx] == '#' else '#'
    return ''.join(updated_diagram)

def expand(diagram, buttons, seen):
    generated_nodes = set()
    for button in buttons:
        updated = apply_button(diagram, button)
        if updated not in seen:
            generated_nodes.add(updated)
    return generated_nodes

result = 0
for row in rows:
    target, buttons, voltages = row
    start = '.' * len(target)
    seen = set()
    seen.add(start)
    current = set()
    current.add(start)
    count = 0
    while target not in seen:
        count += 1
        next = set()
        for diagram in current:
            expanded = expand(diagram, buttons, seen)
            next = next.union(expanded)
        current = next.copy()
        seen = seen.union(current)
    result += count
print(result)


end_time = time.perf_counter()
print(f"Took {end_time - start_time:.4f} seconds")