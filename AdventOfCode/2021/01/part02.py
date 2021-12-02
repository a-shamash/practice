"""--- Day 1: Sonar Sweep ---"""

count = 0

# assuming at least 3 lines
with open('input.txt') as f:
    current_lines = [int(f.readline())]
    current_lines.append(int(f.readline()))
    current_lines.append(int(f.readline()))

    current_sum = sum(current_lines)

    while True:
        next_line = f.readline().strip()
        if not next_line.isnumeric():
            break

        next_lines = current_lines[1:] + [int(next_line)]
        next_sum = sum(next_lines)

        if next_sum > current_sum:
            count += 1

        current_lines = next_lines
        current_sum = next_sum

print(f'Count: {count}')
