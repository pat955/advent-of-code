import math
with open('input.txt', 'r') as file:
    solution = 1
    times, distances = file.readlines()
    for time, distance in zip(times.split()[1:], distances.split()[1:]):
        a, b, c = -1, int(time), -int(distance)
        sol1 = int((-b - math.sqrt((b**2) - (4*a*c)))/(2*a))
        sol2 = int((-b + math.sqrt((b**2) - (4*a*c)))/(2*a))
        solution *= (sol1 - sol2)
        
    print(solution)
        