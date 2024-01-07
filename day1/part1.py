import re

num_sum = 0 
with open("input_file.txt", "r") as input_file:
    for line in input_file:
        first_num = re.search('\d', line).group()
        last_num = re.search('\d', line[::-1]).group()
        num_sum += int(f'{first_num}{last_num}')
        
print(num_sum)