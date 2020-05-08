# A Simple War Game

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    Deck Class for creating a deck of 52 cards
    """
    def __init__(self):
        self.cards = []

        for suite in SUITE:
            for rank in RANKS:
                card = rank + suite
                self.cards.append(card)

    def split(self):
        return self.cards[::2], self.cards[1::2]

    def shuffle(self):
        return shuffle(self.cards)

class Hand:
    '''
    Hand class is used to keep track of the current cards with a player
    '''
    def __init__(self, cards):
        self.cards = cards

    def add(self, cards):
        """
        Expects card as an iterable

        In some cases a single card is supplied as an argument to this function.
        This causes problems when using the insert method because it iterates through the string
        and ends up separating the card letters.
        """
        if (type(cards) != list):	
            cards = [cards]

        shuffle(cards)

        for card in cards:
            self.cards.insert(0, card)

    def remove(self):
        if (len(self) == 0):
            return "Loser"
        else:
            return self.cards.pop()

    def __len__(self):
        return len(self.cards)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return self.name

    def draw_card(self):
        """
        Remove 1 card from hand
        """
        return self.hand.remove()

    def draw_war_cards(self):
        """
        Removes 3 or remaining cards in hand in case of war
        """
        war_cards = []
        if (len(self.hand) < 3):
             for _ in self.hand.cards:
                war_cards.append(self.hand.remove())
        else:
            for _ in range(3):
                war_cards.append(self.hand.remove())
        return war_cards

    def empty(self):
        if not len(self.hand) == 0:
            return True
        else:
            return False

def rank(card):
    if len(card) == 2:
        return RANKS.index(card[0])
    elif len(card) == 3:
        return RANKS.index(card[:2])


def main():

    print("Welcome to War, let's begin...")

    # Instantiating a Deck
    d = Deck()
    d.shuffle()

    h1, h2 = d.split()

    user = Player("User", Hand(h1))
    comp = Player("Computer", Hand(h2))
    
    rounds = 0

    while (user.empty() and comp.empty()):
        rounds += 1

        current_cards = []

        user_card = user.draw_card()
        comp_card = comp.draw_card()

        if "Loser" in user_card or "Loser" in comp_card:
             handle_loser(current_cards, user, comp, user_card, comp_card)

        else:
            current_cards.extend([user_card, comp_card])

            if rank(user_card) > rank(comp_card):
                user.hand.add(current_cards)
            elif rank(user_card) < rank(comp_card):
                comp.hand.add(current_cards)
            else:
                war_routine(current_cards, user, comp)
                #war_single_routine(current_cards, user, comp)

        print("{}. User: {} Comp:{}, Total: {}".format(rounds, len(user.hand), len(comp.hand), len(comp.hand) + len(user.hand)))
        
        if rounds>100_000:
            print("Hand 1:", h1)
            print("Hand 2:", h2)
            break
    
    print()
    print("-"*20)
    if len(user.hand) > len(comp.hand):
    	print("Winner is {}!".format(user))
    elif len(user.hand) < len(comp.hand):
    	print("Winner is {}!".format(comp))
    else:
    	print("Match draw")
    print("-"*20)

def war_routine(current_cards, user, comp):
    # War: Adding 3 face down cards to the current cards #

    user_war_cards = user.draw_war_cards()
    comp_war_cards = comp.draw_war_cards()

    if "Loser" in user_war_cards or "Loser" in comp_war_cards:
        handle_loser(current_cards, user, comp, user_war_cards, comp_war_cards)
    else:
        current_cards.extend(user_war_cards)
        current_cards.extend(comp_war_cards)

        # One face up card for comparing ranks
        user_card = user.draw_card()
        comp_card = comp.draw_card()

        if "Loser" in user_card or "Loser" in comp_card:
            handle_loser(current_cards, user, comp, user_card, comp_card)

        else:
            current_cards.extend([user_card, comp_card])
            
            if rank(user_card) > rank(comp_card):
                user.hand.add(current_cards)
            elif rank(user_card) < rank(comp_card):
                comp.hand.add(current_cards)
            else:
            	war_routine(current_cards, user, comp)
                #war_single_routine(current_cards, user, comp)

def war_single_routine(current_cards, user, comp):
    """
    Handle in war clash, according to the second variation of the game
    """
    # War-Clash: Adding 1 face down card to the current cards ####
    user_card = user.draw_card()
    comp_card = comp.draw_card()

    if "Loser" in user_card or "Loser" in comp_card:
         handle_loser(current_cards, user, comp, user_card, comp_card)

    else:
        current_cards.extend([user_card, comp_card])

        # One face up card for comparing ranks
        user_card = user.draw_card()
        comp_card = comp.draw_card()

        if "Loser" in user_card or "Loser" in comp_card:
             handle_loser(current_cards, user, comp, user_card, comp_card)

        else:
            current_cards.extend([user_card, comp_card])

            if rank(user_card) > rank(comp_card):
                user.hand.add(current_cards)
            elif rank(user_card) < rank(comp_card):
                comp.hand.add(current_cards)
            else:
                war_single_routine(current_cards, user, comp)

def handle_loser(current_cards, user, comp, user_card, comp_card):
    # for strings
    if "Loser" == user_card:
        comp.hand.add(comp_card)
        comp.hand.add(current_cards)

    # for lists
    elif "Loser" in user_card:
        while "Loser" in user_card:
            user_card.remove("Loser")

        comp.hand.add(comp_card)
        comp.hand.add(user_card)

    # for strings
    elif "Loser" == comp_card:
        user.hand.add(user_card)
        user.hand.add(current_cards)

    # for lists
    elif "Loser" in comp_card:
         while "Loser" in comp_card:
             comp_card.remove("Loser")

         user.hand.add(comp_card)
         user.hand.add(user_card)

if __name__ == "__main__":
    main()
