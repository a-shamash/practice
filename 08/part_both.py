"""--- Day 8: Seven Segment Search ---"""

import re

# 1 4 7 8
unique_lengths =[2, 4, 3, 7]
unique_words = '|'.join('[a-h]{' + str(i) + '}' for i in unique_lengths)
unique_words = re.compile(f'\\b({unique_words})\\b')

count = 0

with open('input') as signals:
    for signal in signals:
        signal = signal.split('|')[1]
        count += len(unique_words.findall(signal))        

print(f'Count: {count}')

"""--- Part 2 ---"""

def decode(line):
    line = line.split('|')
    
    str_sort = lambda x: ''.join(sorted(x))
    
    signal = list(map(str_sort, line[1].split()))
    code_words = list(map(str_sort, line[0].split()))
    translation = dict.fromkeys(code_words)
    
    # unique
    one = [c for c in code_words if len(c)==2][0]
    translation[str_sort(one)] = '1'
    four = [c for c in code_words if len(c)==4][0]
    translation[str_sort(four)] = '4'
    seven = [c for c in code_words if len(c)==3][0]
    translation[str_sort(seven)] = '7'
    eight = [c for c in code_words if len(c)==7][0]
    translation[str_sort(eight)] = '8'
    
    # len 6    
    zero_cond = lambda c: len(set(c)-set(four))==3 and len(set(c)-set(seven))==3
    zero = [c for c in code_words if len(c)==6 and zero_cond(c)][0]
    translation[str_sort(zero)] = '0'
    six_cond = lambda c: len(set(c)-set(four))==3 and len(set(c)-set(seven))==4
    six = [c for c in code_words if len(c)==6 and six_cond(c)][0]
    translation[str_sort(six)] = '6'
    nine = [c for c in code_words if len(c)==6 and len(set(four)-set(c))==0][0]
    translation[str_sort(nine)] = '9'
    
    # len 5
    two = [c for c in code_words if len(c)==5 and len(set(four)-set(c))==2][0]
    translation[str_sort(two)] = '2'
    three = [c for c in code_words if len(c)==5 and len(set(one)-set(c))==0][0]
    translation[str_sort(three)] = '3'
    five_cond = lambda c: len(set(four)-set(c))==1 and len(set(c)-set(seven))==3
    five = [c for c in code_words if len(c)==5 and five_cond(c)][0]
    translation[str_sort(five)] = '5'
    
    signal = ''.join(translation[i] for i in signal)    
    
    return int(signal)
    
total = 0
with open('input') as signals:
    for signal in signals:
        total += decode(signal) 

print(f'Total: {total}')
