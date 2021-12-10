"""--- Day 9: Smoke Basin ---"""

risk_levels = []
basin_points = []

def convert_line(line):
    return [10] + [int(i) for i in line] + [10]

def process_line(line, above, below, row):
    risks = []
    loc = []
    
    for pos in range(1, len(current)-1):
        if all(
                [line[pos]<line[pos-1], 
                line[pos]<line[pos+1],
                line[pos]<above[pos],
                line[pos]<below[pos],]
               ):
            risks.append(line[pos]+1)
            loc.append(pos)
    
    return risks, [(row, pos) for pos in loc]


with open('input') as area:
    row = 1
    current = convert_line(area.readline().strip())
    line_length = len(current)
    padding = [10]*line_length
    
    above = padding
    below = convert_line(area.readline().strip())
    
    risks, loc = process_line(current, above, below, row)
    risk_levels += risks
    basin_points += loc
    
    while True:
        above, current = current, below
        below = area.readline().strip()
        
        if not below:
            below = padding
            row +=1
            risks, loc = process_line(current, above, below, row)
            risk_levels += risks
            basin_points += loc
            break
        
        below = convert_line(below)
        row +=1
        risks, loc = process_line(current, above, below, row)
        risk_levels += risks
        basin_points += loc
        
print(f'Risk Levels: {sum(risk_levels)}')

"""--- Part 2 ---"""
from functools import reduce
import re

import numpy as np

with open('input') as area:
    values = area.read()

values = re.sub('[0-8]', '0', values)
values = re.sub('9', '1', values)

# padding
values = re.sub('^', '1', values, flags=re.MULTILINE)
values = re.sub('$', '1', values, flags=re.MULTILINE)
values = values[:-3]

padding = '1'*line_length
values = '\n'.join([padding, values, padding])

values = np.array([[int(i) for i in line] for line in values.split('\n')])

checked_points = set()
basins = []
for dip in basin_points:
    if dip in checked_points:
        continue
    
    to_check = [dip]
    current_basin = set()
    while to_check:
        checking = to_check.pop()
        if checking in current_basin:
            continue
        
        if values[checking[0], checking[1]] == 0:
            current_basin.add(checking)
            to_check.append((checking[0]+1, checking[1]))
            to_check.append((checking[0]-1, checking[1]))
            to_check.append((checking[0], checking[1]+1))
            to_check.append((checking[0], checking[1]-1))
    
    basins.append(len(current_basin))
    checked_points = checked_points.union(current_basin)
    
largest = reduce(lambda x, y: x*y, list(sorted(basins))[-3:])
print(f'Largest: {largest}')
