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
        
    def get_hand_value(self, hand):
        value = 0
        num_aces = 0
        for card in hand:
            if card.value.isnumeric():
                value += int(card.value)
            elif card.value == 'A':
                num_aces += 1
                value += 11
            else:
                value += 10
                
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
                
        return value
    
    def play(self):
        while True:
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)
            
            self.player.show_hand()
            print("Dealer's hand: [{}]".format(self.dealer.hand[0]))
            
            while True:
                action = input("Do you want to hit or stand? ")
                if action == "hit":
                    self.player.draw(self.deck)
                    self.player.show_hand()
                    if self.get_hand_value(self.player.hand) > 21:
                        print("You busted! Dealer wins.")
                        break
                elif action == "stand":
                    break
                else:
                    print("Invalid input, please enter 'hit' or 'stand'.")
            
            while self.get_hand_value(self.dealer.hand) < 17:
                self.dealer.draw(self.deck)
            self.dealer.show_hand()
            
            player_score = self.get_hand_value(self.player.hand)
            dealer_score = self.get_hand_value(self.dealer.hand)
            if player_score > 21:
                print("You busted! Dealer wins.")
            elif dealer_score > 21:
                print("Dealer busted! You win.")
            elif player_score > dealer_score:
                print("You win!")
            elif dealer_score > player_score:
                print("Dealer wins.")
            else:
                print("It's a tie!")
            
            play_again = input("Play again? (y/n): ")
            if play_again == 'n':
                break

    
game = game()
game.play()