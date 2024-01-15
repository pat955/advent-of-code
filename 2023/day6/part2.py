import math
with open('input.txt', 'r') as file:
    time = ''.join(file.readline().split()[1:])
    distance = ''.join(file.readline().split()[1:])

    a, b, c = -1, int(time), -int(distance)
    sol1 = int((-b - math.sqrt((b**2) - (4*a*c)))/(2*a))
    sol2 = int((-b + math.sqrt((b**2) - (4*a*c)))/(2*a))
    solution = sol1 - sol2
        
    print(solution)