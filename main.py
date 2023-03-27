import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(2, 11):
                self.cards.append(Card(suit, str(value)))
            for value in ['J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, value))
                
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()
    
class Player:
    
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.deal())
    
    def show_hand(self):
        print("{}'s hand: {}".format(self.name, self.hand))

class game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Player("Dealer")
    
    def play(self):
        self.player.draw(self.deck)
        self.dealer.draw(self.deck)
        self.player.draw(self.deck)
        self.dealer.draw(self.deck)
        self.player.show_hand()
        self.dealer.show_hand()
    
game = game()

while True:
    game.play()
    play_again = input("Play again? (y/n): ")
    if play_again == 'n':
        break