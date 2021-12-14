"""--- Day 13: Transparent Origami ---"""

import numpy as np

with open('input') as f:
    paper = [i.strip() for i in f]

folds = [i[len('fold along '):].split('=') for i in paper if i.startswith('fold')]
points = {tuple(map(int, p.split(','))) for p in paper[:-len(folds)-1]}

for axis, fold_pt in folds:
    fold_pt = int(fold_pt)
    
    if axis=='x':
        points = {(2*fold_pt - x if x> fold_pt else x, y) for x,y in points if x!=fold_pt}
    else:
        points = {(x, 2*fold_pt - y if y> fold_pt else y) for x,y in points if y!=fold_pt}

points = list(points)
points = ([x for x,y in points],
          [y for x,y in points])
x_max = max(points[0])
y_max = max(points[1])

message = np.zeros((x_max+1, y_max+1))
message[points] = 1

message = message.transpose()
