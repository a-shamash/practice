#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:32:43 2022

@author: adam
"""

luggage_score: int = 0
badge_score: int = 0

groups = [None]*3

def priority_score(matched):
    i = ord(matched)
    return i-38 if i<96 else i - 96
    
with open('input') as cargo:
    idx = 0
    while bag:=cargo.readline():
        groups[idx] = bag.strip()
        
        comp1 = bag[:len(bag)//2]
        comp2 = bag[len(bag)//2:-1]
        
        matched = [c for c in comp1 if c in comp2][0]
                
        luggage_score += priority_score(matched)
        
        if idx==2:
            matched_group = [c for c in groups[0] if c in groups[1] and c in groups[2]][0]
            badge_score += priority_score(matched_group)
            idx = 0
        else:
            idx += 1
        
print('Part 1:', luggage_score)
print('Part 2:', badge_score)
