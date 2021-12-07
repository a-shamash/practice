"""--- Day 5: Hydrothermal Venture ---"""

from collections import Counter


PERIOD = 7
CHILDHOOD = 2
DAYS = 256

fish = Counter([int(i) for i in open('input').read().split(',')])
fish = {k: fish.get(k, 0) for k in range(PERIOD+CHILDHOOD)}

for day in range(DAYS):
    fish = {k-1: v for k, v in fish.items()}
    fish[PERIOD-1+CHILDHOOD] = fish[-1]
    fish[PERIOD-1] += fish[-1]
    del fish[-1]

total = sum([i for i in fish.values()])
print(f'Fish: {total}')
