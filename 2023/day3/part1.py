import re
SYMBOLS = ['#', '%', '*', '$', '£', '@', '&', '?', '+', '-', '/', '=']

def symbol_adjecent(text, i, start, end):
    if start != 0:
        if text[i][start-1] in SYMBOLS:
            return True
    else:
        start -= 1 
    
    if end != 140:
        if text[i][end] in SYMBOLS:
            return True
    else:
        end -= 1

    for j in range(start-1, end +1):
        if i != 0:
            if text[i-1][j] in SYMBOLS:
                return True
        if i != len(text)-1:
            if text[i+1][j] in SYMBOLS:
                return True
    return False

with open('input.txt', 'r') as file:
    text = file.read().split('\n')
    total = 0
    i = 0
    for line in text:
        for match in re.finditer(r'\d+', line):
            if symbol_adjecent(text, i, match.start(), match.end()):
                total += int(match.group())       
        i += 1
    print(total)