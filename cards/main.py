"""
    The Goal of this program is to generate a deck of cards.
    Ideally it will do so in "New Deck Format"
    It would be cool if I could shuffle the deck.
    It would be cool if I could deal some cards.
"""

import random


def main():
    """ Let's use this function for control flow, input and outputs"""
    print(f"Generating a new deck.")
    card_deck = new_deck()
    #print(f'{card_deck}')  #This will be new deck order.

    shuffle_deck(card_deck)
    #print(f'{card_deck}')  #This will be shuffled.
    deal_cards(card_deck)


def new_deck():
    """ 
        This function should generate a new deck
        New Deck Order is: Joker1, Joker 2,
                            A->K Spades 
                            A->K Diamonds 
                            A->K Clubs 
                            A->K Hearts 
    """
    my_deck = [] 
    for suit in ("S", "D", "C", "H"):
        for value in ("A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"):
            my_deck.append(f'{value}{suit}')
    return my_deck


def shuffle_deck(card_deck):
    """
        This function should take the deck in whatever order it is
        and shuffle it.
    """
    shuffled_deck = random.shuffle(card_deck)
    

def deal_cards(my_deck):
    """
        This should take an integer as an input and deal that number
        of cards to each player.  Which means we should also accept a
        number of players as an input as well.
    """
    choice_one = random.choice(my_deck)
    my_deck.remove(choice_one)
    choice_two = random.choice(my_deck)
    my_deck.remove(choice_two)
    print(f'{choice_one}, {choice_two}, {len(my_deck)}')



if __name__ == '__main__':
    main()
