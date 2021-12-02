"""--- Day 1: Sonar Sweep ---"""

count = 0

with open('input.txt') as f:
    current_line = int(f.readline())
    while True:
        next_line = f.readline().strip()
        if not next_line.isnumeric():
            break
        
        next_line = int(next_line)
        
        if next_line > current_line:
            count += 1
        current_line = next_line

print(f'Count: {count}')