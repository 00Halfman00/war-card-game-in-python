import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
    'Jack':11, 'Queen':12, 'King':13, 'Ace':14
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    # to print card
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:                            # for each element in the suits list
            for rank in ranks:                        # for each element in suits we will mix it with every element in ranks
                self.all_cards +=[Card(suit, rank)]   # Two of Hearts, Three of Hearts, Four of Hearts, etc...
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards += new_cards               # if the new_cards passed in are in a list add one list to another
        else:
            self.all_cards += [new_cards]             # if the new_cards passed in is just a card object add it inside a list
            
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#####################################################################################################start of game
game_deck = Deck()                                    # create a deck of 52 cards
game_deck.shuffle()                                   # shuffle the 52 game cards
player_one = Player('one')                            # create player one
player_two = Player('two')                            # create player two

while game_deck.all_cards:                            # split the deck of cards between player one and player two
    if not game_deck.all_cards[0]:
        break
    player_one.add_cards(game_deck.deal_one())
    if not game_deck.all_cards[0]:
        break
    player_two.add_cards(game_deck.deal_one())

'''code below is the game logic'''

round = 0
game = True

while game:
    round += 1
    print(f'Round {round}')

    if not len(player_one.all_cards):                   # check to see if player one still has cards to play else he loses
        print('Player one is out of cards')
        print('Player Two wins! Game Over')
        game = False
        break

    if not len(player_two.all_cards):                   # check to see if player two still has cards to play else he loses
        print('Player two is out of cards')
        print('Player One wins! Game Over')
        game = False
        break

    player_one_cards = []
    player_one_cards += [player_one.remove_one()]

    player_two_cards = []
    player_two_cards += [player_two.remove_one()]

    war = True
    while war:

        if player_one_cards[-1].value > player_two_cards[-1].value:   # if player one has the highest card, he adds both cards drawn to his deck
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            war = False

        if player_two_cards[-1].value > player_one_cards[-1].value:   # if player two has the highest card, he adds both cards drawn to his deck
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            war = False
    
        else:                                           # if there is a tie in card value/s then 'WAR', so draw five cards to place on next bet
            print('WAR!')

            if len(player_one.all_cards) < 5:           # if player one does not have at least five more cards, then go home
                print('Player one is out of cards')
                print('Player Two wins the game')
                game = False
                break

            if len(player_two.all_cards) < 5:           # if player two does not have at least five more cards, then go home
                print('Player two is out of cards')
                print('Player One wins the game')
                game = False
                break

            else:                                       # if both players have atleast five more cards, then draw five each by adding to their game cards
                for num in range(5):
                    player_one_cards += [player_one.remove_one()]
                    player_two_cards += [player_two.remove_one()]
