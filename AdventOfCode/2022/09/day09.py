#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:40:44 2022

@author: adam
"""

motion = dict()

KNOTS = 9

head = (0, 0)
tail_knots = [head] + [head]*KNOTS
tail_pos = [{tail_knots[i]} for i in range(KNOTS+1)]

def three_way_equality(a, b):
    if a<b:
        return -1
    elif a==b:
        return 0
    return 1

def update_tail(h, t):
    'h=head; t=tail'
    if abs(h[0]-t[0])<=1 and abs(h[1]-t[1])<=1:
        return t
    
    if abs(h[0]-t[0])<=1:
        ver = 0
        hor = three_way_equality(h[1], t[1])
    elif abs(h[1]-t[1])<=1:
        ver = three_way_equality(h[0], t[0])
        hor = 0
    else:
        ver = three_way_equality(h[0], t[0])
        hor = three_way_equality(h[1], t[1])
    
    return (h[0]-ver, h[1]-hor)


count = 0
for line in open('input'):
    direction, steps = line.strip().split()
    for i in range(int(steps)):
        head = list(tail_knots[0])
        match direction:
            case 'L':
                head[1] -= 1
            case 'R':
                head[1] += 1
            case 'D':
                head[0] -= 1
            case 'U':
                head[0] += 1
            
        tail_knots[0] = tuple(head)
        tail_pos[0].add(tail_knots[0])
        
        for knot in range(1, KNOTS+1):
           tail_knots[knot] = update_tail(tail_knots[knot-1], tail_knots[knot])
           tail_pos[knot].add(tail_knots[knot])


print('Part 1:', len(tail_pos[1]))
print('Part 2:', len(tail_pos[-1]))
