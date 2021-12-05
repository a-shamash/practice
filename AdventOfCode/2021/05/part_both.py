"""--- Day 5: Hydrothermal Venture ---"""

from collections import Counter

vent_positions = Counter()

# set up
with open('input') as f:
    for vent in f:
        start, end = vent.split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        
        if x1==x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            vent_positions.update((x1, y) for y in range(y1, y2+1))
        elif y1==y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            vent_positions.update((x, y1) for x in range(x1, x2+1))
        else:
            # comment out for part 1
            step_x = 1 if x1<x2 else -1
            step_y = 1 if y1<y2 else -1
            vent_positions.update((x, y) for x, y 
                                          in zip(
                                              range(x1, x2+step_x, step_x),
                                              range(y1, y2+step_y, step_y)
                                              )
                                  )

danger = len([k for k, v in vent_positions.items() if v>=2])
print(f'Danger Zones: {danger}')
