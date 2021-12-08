"""--- Day 7: The Treachery of Whales ---"""

with open('input') as f:
    crabs = [int(i) for i in f.read().split(',')]

crabs_len = len(crabs)
crabs = sorted(crabs)

if crabs_len%2:
    medium_pos_lower = medium_pos_upper = crabs_len//2
else:
    medium_pos_lower = crabs_len//2 -1
    medium_pos_upper = medium_pos_lower

medium = (crabs[medium_pos_lower] + crabs[medium_pos_upper])//2

fuel = sum(map(lambda x: abs(x-medium), crabs))
print(f'Medium: {fuel}')

"""--- Part Two ---"""
mean = round(sum(crabs)/crabs_len)

fuel_cost = lambda pos: sum(map(lambda x: abs(x-pos)*(abs(x-pos)+1)/2, crabs))
fuel = fuel_cost(mean)

direction = -1**(mean<medium)
for pos in range(mean+direction, medium+direction, direction):
    if fuel_cost(pos) < fuel:
        fuel = fuel_cost(pos)

print(f'Mean: {fuel}')