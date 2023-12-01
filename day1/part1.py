import re

num_lst = []
with open("input_file.txt", "r") as input_file:
    for line in input_file:
        first_num = re.search('\d', line).group()
        last_num = re.search('\d', line[::-1]).group()
        num_lst.append(int(f'{first_num}{last_num}'))
        
print(sum(num_lst))