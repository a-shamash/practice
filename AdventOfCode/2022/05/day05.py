#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:24:11 2022

@author: adam
"""

check_crates = True
crates = ''

for line in open('input'):
    if check_crates:
        if line.startswith(' 1'):
            check_crates = False
            levels = [[c_row[i] for i in range(1, len(c_row), 4)] for c_row in crates.split('\n')[:-1]]
            rows = len(levels[-1])
            crates = [[level[i] for level in reversed(levels) if level[i]!=' '] for i in range(rows)]
            crates_part2 = [c.copy() for c in crates]
            continue
        crates += line
        continue
    
    try:
        line = line.split()
        move = int(line[1])
        origin = int(line[3])-1
        dest = int(line[5])-1
        
        # Part 1
        for i in range(move):
            crates[dest].append(crates[origin].pop())
            
        # Part 2            
        crates_cranned = crates_part2[origin][-move:].copy()
        crates_part2[origin] = crates_part2[origin][:-move]
        crates_part2[dest] += crates_cranned
            
    except IndexError:
        continue

print('Part 1:', ''.join([i[-1] for i in crates]))
print('Part 2:', ''.join([i[-1] for i in crates_part2]))
