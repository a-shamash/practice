#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 20:08:22 2022

@author: adam
"""

FILE_LIMIT = 100000
TOTAL_SIZE = 70000000
NEEDED = 30000000

current_path = list()
file_struct = dict()
directories = set()

with open('input') as cmd_list:
    while cmd := cmd_list.readline():        
        cmd = cmd.strip().split()
        match cmd[1]:
            case 'cd':
                if cmd[-1] == '..':
                    current_path = current_path[:-1]
                else:
                    current_path.append(cmd[-1])
                    directories.add(r'/'.join(current_path))
            case 'ls':
                    
                while file := cmd_list.readline():
                    file = file.strip().split()
                    
                    if file[0] == 'dir':
                        continue
                    elif file[1]=='cd' and file[0]=='$':
                        if file[-1] == '..':
                            current_path = current_path[:-1]
                        else:
                            current_path.append(file[-1])
                            directories.add(r'/'.join(current_path))
                        break
                    
                    else:
                        file_path = r'/'.join(current_path+[file[-1]])
                        file_struct[file_path] = int(file[0])

size_dir = dict.fromkeys([r'/'.join(i.split(r'/')[:-1]) for i in file_struct.keys()], 0)
size_dir = dict.fromkeys(directories, 0)
true_size_dir = size_dir.copy()
for file, size in file_struct.items():
    for dir_key in size_dir.keys():
        if file.startswith(dir_key):
            size_dir[dir_key] += size

print('Part 1:', sum([s for s in size_dir.values() if s<FILE_LIMIT]))


available = TOTAL_SIZE-size_dir['/']
to_delete = NEEDED-available
smallest = min([s for s in size_dir.values() if s>=to_delete])

print('Part 2:', smallest)
