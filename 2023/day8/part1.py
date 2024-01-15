def traverse(ghost_map, instructions, location):
    i, steps = -1, 0 
    
    while location != 'ZZZ':
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

    print(traverse(ghost_map, instructions.strip(), 'AAA'))
