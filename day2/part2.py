from math import prod

def find_minimums(sets):
    colors = {'red': 0, 'green': 0, 'blue': 0}
    for cubes in sets.strip('\n').replace(';', ',').split(', '):
        num, color = cubes.split(' ')
        if colors[color] < int(num):
            colors[color] = int(num)

    return colors.values()

with open("input_file.txt", "r") as file:
    total_min_power = 0
    for line in file:
        game, sets= line.split(': ')
        total_min_power += prod(find_minimums(sets))

    print(total_min_power)
        
        