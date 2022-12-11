#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:35:23 2022

@author: adam
"""

import numpy as np

cycle = 1
register = 1

# part1
important_signals = (20, 60, 100, 140, 180, 220)
important_signals = dict.fromkeys(important_signals)

# part2
display = np.zeros((6, 40))
current_row = 0

def cycle_increase(register):
    global cycle
    global display
    global current_row
    
    cycle += 1
    if cycle in important_signals:
        important_signals[cycle] = register
    
    if cycle%40 == 0:
        current_row+=1
    
    if (cycle-1)%40 -1 <= register and register <= (cycle-1)%40 +1:
        display[current_row, (cycle-1)%40] = 1
    
    return cycle


for signal in open('input'):
    if signal.startswith('noop'):
        cycle_increase(register)       
        continue
    
    cycle_increase(register)
    
    _, addx = signal.split()
    register += int(addx)
    
    cycle_increase(register)
    
print('Part 1:', sum([k*v for k,v in important_signals.items()]))
print('Part 2:')
for row in display:
    for col in row:
        print('#' if col else ' ', end='')
    print()
