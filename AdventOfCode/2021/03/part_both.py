"""--- Day 3: Binary Diagnostic ---"""

def adjust_gamma(current, signal, signal_size):
    signal = map(int, signal.strip())
    return [c + (1 if s else -1) for c, s in zip(current, signal)]

line_count = 0  # for part 2

with open('input', 'r') as report:
    signal = report.readline()
    signal_size = len(signal)
    gamma = [0]*signal_size
    
    while signal:
        line_count +=1
        gamma = adjust_gamma(gamma, signal, signal_size)
        signal = report.readline()

gamma = [int(i>0) for i in gamma]
epsilon = [int(not i) for i in gamma]

gamma = ''.join(map(str, gamma))

epsilon = ''.join(map(str, epsilon))

print(f'Power: {int(gamma, 2)*int(epsilon, 2)}')

"""--- Part Two ---"""

o2_start = gamma[0]
co2_start = epsilon[0]

with open('input', 'r') as report:
    possible = range(line_count)
    o2_values = []
    co2_values = []
    for line_num in possible:
        report.seek(signal_size*line_num)
        if report.read(1) == o2_start:
            o2_values.append(line_num)
        else:
            co2_values.append(line_num)
    
    # get o2 value
    for pos in range(1, signal_size):
        zeros = []
        ones = []
        for line_num in o2_values:
            report.seek(signal_size*line_num+pos)
            if report.read(1) == '1':
                ones.append(line_num)
            else:
                zeros.append(line_num)
            
        if len(zeros) <= len(ones):
            o2_values = ones
        else:
            o2_values = zeros
        
        if len(o2_values) == 1:
            break
    
    report.seek(signal_size*o2_values[0])
    o2_level = report.read(signal_size).strip()
    
    # get co2 value
    for pos in range(1, signal_size):
        zeros = []
        ones = []
        for line_num in co2_values:
            report.seek(signal_size*line_num+pos)
            if report.read(1) == '1':
                ones.append(line_num)
            else:
                zeros.append(line_num)
            
        if len(zeros) <= len(ones):
            co2_values = zeros
        else:
            co2_values = ones
        
        if len(co2_values) == 1:
            break
    
    report.seek(signal_size*co2_values[0])
    co2_level = report.read(signal_size).strip()

print(f'Life Support: {int(o2_level, 2)*int(co2_level, 2)}')
