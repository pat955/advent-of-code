import re
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
NON_NUMS = ['.', '%', '/', '#', '@', '&', '$', '=', '+', '-']

def gear_ratio(text, i, j):
    adjecent_amount = get_adjecent(text, i, j)
    if len(adjecent_amount) == 2:
        return int(adjecent_amount[0])* int(adjecent_amount[1])
    return 0  


def middle_ifs(text, i, j, adjecent, row):
    if row[j] in NUMS and row[j-1] in NON_NUMS:
        adjecent.append(re.match('\d+', row[j:]).group())
        
    elif row[j] in NUMS and row[j+1] in NON_NUMS:
        adjecent.append(''.join((list(reversed(re.findall('\d+', ''.join(list(reversed(row[:j+1]))))[0])))))

    elif row[j] in NUMS:
        adjecent.append(re.match('\d+', row[j-1:j+2]).group())
        
    return adjecent

def get_adjecent(text, i, j):
    row = text[i]
    upper_row = text[i-1]
    lower_row = text[i+1]
    adjecent = []

    if row[j+1] in NUMS:
        adjecent.append(re.match('\d+',row[j+1:]).group())
    if row[j-1] in NUMS:
        adjecent.append(''.join((list(reversed(re.match('\d+', ''.join(list(reversed(row[:j])))).group())))))

    if upper_row[j+1] in NUMS and upper_row[j] in NON_NUMS:
        adjecent.append(re.match('\d+', upper_row[j+1:]).group())

    if upper_row[j-1] in NUMS and upper_row[j] in NON_NUMS:
        adjecent.append(''.join((list(reversed(re.findall('\d+', ''.join(list(reversed(upper_row[:j]))))[0])))))

    adjecent = middle_ifs(text, i, j, adjecent, upper_row)
    
    if lower_row[j+1] in NUMS and lower_row[j] in NON_NUMS:
        adjecent.append(re.match('\d+', lower_row[j+1:]).group())

    if lower_row[j-1] in NUMS and lower_row[j] in NON_NUMS:
        adjecent.append(''.join((list(reversed(re.findall('\d+', ''.join(list(reversed(lower_row[:j]))))[0])))))
    adjecent = middle_ifs(text, i, j, adjecent, lower_row)
    return adjecent

with open('input.txt', 'r') as file:
    text = [144*'.'] 
    text.extend(file.read().split('\n'))
    i = 0    
    for line in text:
        row = '..'+line+'..' 
        i += 1
    text.append(144*'.')
    total = 0
    i = 0
    for line in text:
        for match in re.finditer(r'[*]', line):
            total += gear_ratio(text, i, match.start())  
        i += 1
    print(total)