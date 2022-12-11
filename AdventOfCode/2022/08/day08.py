#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  10 18:38:13 2022

@author: adam
"""

import numpy as np

trees = list()

for line in open('input'):
    trees.append([int(i) for i in line.strip()])

FOREST_HEIGHT = len(trees)
FOREST_WIDTH = len(trees[0])

trees = np.array(trees)

# 0 left, 1 up, 2 right, 3 down
visibility = np.empty((FOREST_HEIGHT, FOREST_WIDTH, 4),)

for direction in range(4):
    visibility[:, 0, direction] = True
    tallest = trees[:, 0].copy()
    
    for col in range(1, trees.shape[0]):
       visibility[:, col, direction] = (tallest < trees[:, col])
       tallest = np.maximum(tallest, trees[:, col])
       
    trees = np.rot90(trees)
    visibility = np.rot90(visibility)

visibility_levels = np.sum(visibility, axis=2)
print('Part 1:', (visibility_levels!=0).sum())

max_score = 0

for height in range(1, 10):
    potential_house = trees[1:FOREST_HEIGHT, 1:FOREST_WIDTH]
    house = np.transpose(np.nonzero(potential_house == height))+1
    scenery = trees >= height
    
    for row, col in house:
        left = col-x[-1] if len(x:=np.flatnonzero(scenery[row, :col])) else col
        right = x[0]+1 if len(x:=np.flatnonzero(scenery[row, col+1:])) else FOREST_WIDTH-col-1
        
        up = row - x[-1] if len(x:=np.flatnonzero(scenery[:row, col])) else row
        down = x[0]+1 if len(x:=np.flatnonzero(scenery[row+1:, col])) else FOREST_HEIGHT-row-1
        
        max_score = max(max_score, left*right*up*down)
    
print('Part 2:', max_score)
    