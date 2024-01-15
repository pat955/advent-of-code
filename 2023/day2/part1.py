def is_possible(sets):
    for collection in sets.strip('\n').split('; '):
        for cubes in collection.split(', '):
            colors = {'red': 0, 'green': 0, 'blue': 0}
            num, color = cubes.split(' ')
            colors[color] += int(num)
            if colors['red'] > 12 or colors['green'] > 13 or colors['blue'] > 14:
                return False
    return True

with open("input_file.txt", "r") as file:
    possible_sum = 0 
    for line in file:
        game, sets= line.split(': ')
        if is_possible(sets):
            possible_sum += int(game.strip('Game '))
    print(possible_sum)


