#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:38:13 2022

@author: adam
"""

from collections import deque

MARKER_LEN = 14

with open('input') as mess:
    marker = deque('_'+mess.read(MARKER_LEN-1))
    for pos, c in enumerate(mess.read()):
        marker.append(c)
        marker.popleft()
        if len(set(marker))==MARKER_LEN:
            break
    pos += MARKER_LEN

print(f'Marker Size {MARKER_LEN}:', pos)
