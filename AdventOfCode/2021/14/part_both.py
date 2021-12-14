"""--- Day 14: Extended Polymerization ---"""

from collections import Counter

STEPS = 40

insertions = dict()

with open('input') as f:
    poly = f.readline().strip()
    f.readline()
    for insert in f:
        insert = insert.strip().split(' -> ')
        insertions[insert[0]] = insert[1]

poly = '~' + poly
poly = Counter([poly[i:i+2] for i in range(len(poly)-1)])

for step in range(STEPS):
    additions = dict()
    deletions = dict()
    
    for insert, insert_value in insertions.items():
        if insert in poly:
            additions.setdefault(insert[0]+insert_value, 0)
            additions[insert[0]+insert_value] += poly[insert]  
            
            additions.setdefault(insert_value+insert[1], 0)
            additions[insert_value+insert[1]] += poly[insert]  
            
            deletions[insert] = -poly[insert]
        
    poly.update(additions)
    poly.update(deletions)

letters = dict.fromkeys(set(i[1] for i in poly.keys()), 0)
for let in letters.keys():
    letters[let] = sum([v for k,v in poly.items() if k[1]==let])
difference = max(list(letters.values())) - min(list(letters.values()))

print(f'Diff: {difference}')
