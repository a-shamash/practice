#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:32:43 2022

@author: adam
"""

first_score = second_score = 0

with open('input') as luggage:
    while seq := luggage.readline():
        opponent, you = map(lambda x: ord(x)-64, seq.split())
        you = you-23
        
        first_score += you + 3*((you-opponent+1)%3)
        
        choice_position = (opponent + (you-2))%3
        choice_position = choice_position if choice_position else 3
        second_score += choice_position + ((you-1)%3)*3

print('First Strategy:', first_score)
print('Second Strategy:', second_score)
