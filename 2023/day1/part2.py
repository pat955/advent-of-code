import re

num_sum = 0
regex_str = '\d|one|two|three|four|five|six|seven|eight|nine'
num_words_to_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
with open('input_file.txt', 'r') as input_file:
    for line in input_file:
        first_num = re.search(regex_str, line).group()
        last_num = re.search('\d|'+(regex_str[:2:-1]), line[::-1]).group()[::-1]

        if first_num in num_words_to_num:
            first_num = num_words_to_num[first_num]

        if last_num in num_words_to_num:
            last_num = num_words_to_num[last_num]

        num_sum += (int(f'{first_num}{last_num}'))
print(num_sum)