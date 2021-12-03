"""--- Day 2: Dive! ---"""

distance, depth = 0, 0


with open('input.txt') as f:
    current_dir = f.readline()
    while current_dir:
        direction, value = current_dir.split()
        value = int(value)
        
        if direction == 'forward':
            distance += value
        else:
            depth += value* (1 if direction=='down' else -1)
        current_dir = f.readline()

print('Part 1')
print(f'Distance: {distance}')
print(f'Depth: {depth}')
print(f'Answer: {distance*depth}')
print()

"""--- Part Two ---"""
distance, depth, aim = 0, 0, 0


with open('input.txt') as f:
    current_dir = f.readline()
    while current_dir:
        direction, value = current_dir.split()
        value = int(value)
        
        if direction == 'forward':
            distance += value
            depth += value*aim
        else:
            aim += value* (1 if direction=='down' else -1)
        current_dir = f.readline()

print('Part 2')
print(f'Distance: {distance}')
print(f'Depth: {depth}')
print(f'Answer: {distance*depth}')
print()
