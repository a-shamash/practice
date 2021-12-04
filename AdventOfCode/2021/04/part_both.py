"""--- Day 4: Giant Squid ---"""

import re

# set up
with open('input') as f:
    calls = f.readline()
    tables = f.read()

calls = map(int, calls.split(','))

tables = tables.strip().split('\n\n')
tables = [[int(i) for i in re.split('[\n ]', t) if i] for t in tables]
original = tables.copy()

def check_table(table):
    # True if winner
    # horizontal
    for i in range(5):
        if sum(table[i*5:(i+1)*5]) == -5:
            return True
    
    for i in range(5):
        if sum(table[i:25:5]) == -5:
            return True
    
    return False

# make calls
for call in calls:
    tables = [[-1 if i==call else i for i in table] for table in tables]
    results = [check_table(table) for table in tables]
    if any(results):
        winner = results.index(True)
        break

winning_table = tables[winner]
score = call * sum(i for i in winning_table if i>0)
print(f'Winner Score: {score}')

# check rest of boards
for call in calls:
    tables = [[-1 if i==call else i for i in table] for table in tables]
    results = [not check_table(table) for table in tables]
    if sum(results) == 1:
        loser = results.index(True)
        break

losing_table = tables[loser]
for call in calls:
    losing_table = [-1 if i==call else i for i in losing_table]
    if check_table(losing_table):
        break

score = call * sum(i for i in losing_table if i>0)
print(f'Loser Score: {score}')
