#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:32:43 2022

@author: adam
"""

calories = [0]
with open('input') as luggage:
    while food := luggage.readline():
        match food:
            case '\n':
                calories.append(0)
            case _:
                calories[-1] += int(food)

calories = sorted(calories)

print('Max Calories:', calories[-1])
print('Total Calories:', sum(calories[-3:]))
