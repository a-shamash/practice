#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:46:12 2022

@author: adam
"""

part1 = 0
part2 = 0

with open('input') as assignments:
    while pair:=assignments.readline().strip():
        elf1, elf2 = [list(map(int, a.split('-'))) for a in pair.split(',')]
        
        if (elf1[0]==elf2[0]) or (elf1[1]==elf2[1]):
            part1 += 1
            part2 += 1
        elif (elf1[0]<elf2[0]) == (elf1[1]>elf2[1]):
            part1 += 1
            part2 += 1
        elif (elf1[1]==elf2[0]) or (elf1[0]==elf2[1]):
            part2 += 1
        elif (elf2[0]<elf1[1]) and (elf1[1]<elf2[1]):
            part2+= 1
        elif (elf1[0]<elf2[1]) and (elf2[1]<elf1[1]):
            part2+= 1

print('Part 1', part1)
print('Part 2', part2)
