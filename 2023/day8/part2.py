import math
def traverse(ghost_map, instructions, location):
    i, steps = -1, 0 
    
    while location[-1] != 'Z':
        steps += 1
        if i >= len(instructions)-1:
            i = -1 
        i += 1 
        
        if instructions[i]== 'R':
            location = ghost_map[location][1]
        
            
        elif instructions[i] == 'L':
            location = ghost_map[location][0]
    return steps

with open('input.txt', 'r') as file:
    instructions = file.readline()
    lines = (file.read().split('\n'))
    ghost_map = {line[0:3]: tuple(line[7:-1].split(', ')) for line in lines[1:]}

    steps = []
    for starting_location in [k for k in ghost_map.keys() if k[-1] == 'A']:
        steps.append(traverse(ghost_map, 'R', starting_location))
        steps.append(traverse(ghost_map, 'L', starting_location))
    
    print(math.lcm(tuple(steps)))
