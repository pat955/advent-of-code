import re

with open('test.txt', 'r') as file:
    rank_list = []
    for line in file:
        hand, bet = line.split()
        

def get_type(hand):
    first_card = hand[0]
    if hand == first_card*5:
        return ((4, first_card))
    