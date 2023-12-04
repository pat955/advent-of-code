with open('input.txt', 'r') as file:
    total_points = 0 
    for line in file:
        points = 0
        
        winning_nums = [i for i in line[9:40].split(' ') if i]
        card_nums = [i for i in line[41:].split(' ') if i]
    
        if '\n' in card_nums[-1]:
            card_nums[-1] = card_nums[-1][:-1]

        for num in card_nums: 
            if num in winning_nums:
                if points == 0:
                    points += 1
                else:
                    points*=2
        total_points += points
    print(total_points)