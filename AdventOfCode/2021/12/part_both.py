"""--- Day 12: Passage Pathing ---"""

SMALL_ONCE = False  # True for Part 1, False for Part 2

with open('input') as f:
    connectors = f.read()

connectors = [i.split('-') for i in connectors.split('\n') if '-' in i]
caves = set(sum(connectors, []))

begin = lambda c: set(p[1] for p in connectors if p[0]==c)
end = lambda c: set(p[0] for p in connectors if p[1]==c)
connectors = {c: begin(c).union(end(c)) for c in caves}
for cave, c in connectors.items():
    if 'start' in c:
        connectors[cave].remove('start')


ongoing = [(SMALL_ONCE, ['start'])]
complete = []

while ongoing:
    small_limit, base = ongoing.pop()
    next_caves = {c for c in connectors[base[-1]]}
    
    complete += [base + [c] for c in next_caves if c == 'end']
    
    if 'end' in next_caves:
        next_caves.remove('end')
    
    if small_limit or [c for c in base if c.islower() and base.count(c)==2]:
        small_limit = True
    
    if small_limit:
        next_caves = {c for c in next_caves if c.isupper() or c not in base}
    
    ongoing += [(small_limit, base + [c]) for c in next_caves if c != 'end']

print(f'Paths: {len(complete)}')

test = [[c for c in i if c.islower() and i.count(c)>1] for i in complete]
