"""--- Day 10: Syntax Scoring ---"""

from functools import reduce

SCORES = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

PAIRS = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

illegal_scores = []
incomplete_scores = []

def illegal_score(line):
    stack = []
    for c in line:
        if c in '({[<':
            stack.append(c)
        else:
            if not stack:
                return SCORES[c]
            
            if ord(c)-ord(stack[-1])<3 and ord(c)-ord(stack[-1])>0:
                stack.pop()
                continue
            
            return SCORES[c], stack

    return 0, stack

def incomplete_score(remaining):
    closing = map(lambda x: PAIRS[x], reversed(remaining))
    score = reduce(lambda x, y: x*5+y, closing)
    return score

with open('input') as f:
    for line in f:
        illegal, remaining = illegal_score(line.strip())
        if illegal:
            illegal_scores.append(illegal)
        else:
            incomplete_scores.append(incomplete_score(remaining))

incomplete_scores = list(sorted(incomplete_scores))
middle = incomplete_scores[len(incomplete_scores)//2]

print(f'Illegal: {sum(illegal_scores)}')
print(f'Incomplete: {middle}')
