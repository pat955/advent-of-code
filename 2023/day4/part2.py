with open('input.txt', 'r') as file:
    all_cards = file.read().split('\n')
    cards = [1 for i in all_cards]
    
    for index, line in enumerate(all_cards):
        line = line.split(":")[1]
        
        winning_nums, our_nums = line.split("|")
        winning_nums, our_nums = winning_nums.split(), our_nums.split()
        matches = len(set(winning_nums) & set(our_nums))
        
        for i in range(matches):
            cards[index + i + 1] += cards[index]

    print(sum(cards))


    