import re
def main():
    
    with open('input.txt', 'r') as file:
        rank_dict = {}
        for line in file:
            hand, bet = line.split()
            get_type(hand)
            
        

def get_type(hand):
    hand_hierarchy = {
        'Five of a kind',
        'Four of a kind',
        'Full house',
        'Three of a kind',
        'Two pair',
        'One pair',
        'High card'
    }
    values =['A','2','3','4','5','6','7','8','9','T','J','Q','K']

    hand_sorted = sorted([*hand], key=values.index)
    print(hand_sorted)
    hand_set = set([*hand])
    hand_length = len(hand_set)

    if hand_length == 0:
        return (hand[0], 'Five of a kind')
    
    if hand_length == 2:
        first_card = hand[0]
        first_card_count = [*hand].count(first_card)
        if first_card_count == 4:
            return (first_card, 'Four of a kind')

        elif first_card_count == 1:
            return (hand[1], 'Four of a kind')
        else:
            return ('Fullhouse')

    if hand_length == 3:
        pass

    

def partition(rank_dict):
    pass

def quicksort(rank_dict):
    pass


main()