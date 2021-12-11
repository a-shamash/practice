"""--- Day 11: Dumbo Octopus ---"""

import numpy as np

STEPS = 100

with open('input') as f:
    octopuses = f.read()

octopuses = np.array([[int(i) for i in line] for line in octopuses.split('\n') if line])
X_LIM, Y_LIM = octopuses.shape

flash_count = 0
synchro_step = False

step = 0
while not synchro_step or step < STEPS:
    octopuses += 1
    
    flashes = np.where(octopuses == 10)
    flashes = [(x, y) for  x, y in zip(*flashes)]
    flashed = set()
    while flashes:
        flash_x, flash_y = flashes.pop()
        
        flashed.add((flash_x, flash_y))
        
        x_min = max(0, flash_x-1)
        y_min = max(0, flash_y-1)
        x_max = min(flash_x+2, X_LIM)
        y_max = min(flash_y+2, Y_LIM)
        
        test = octopuses[x_min:x_max, y_min:y_max].copy()
        octopuses[x_min:x_max, y_min:y_max] += 1
        test2 = octopuses[x_min:x_max, y_min:y_max].copy()
        new_flashes = np.where(octopuses[x_min:x_max, y_min:y_max] == 10)
        
        shift_x = flash_x if flash_x==0 else flash_x-1
        shift_y = flash_y if flash_y==0 else flash_y-1
        
        flashes += [(x+shift_x, y+shift_y) for  x, y in zip(*new_flashes)]
        
    if flashed:
        if step<STEPS:
            flash_count += len(flashed)
            
        flashed = (np.array([x for x, y in flashed]),
                   np.array([y for x, y in flashed]),)
        octopuses[flashed] = 0
        
    
    if not synchro_step and len(np.unique(octopuses))==1:
        synchro_step = step+1
    
    step +=1

print(f'Flashes: {flash_count}')
print(f'Synchro: {synchro_step}')
