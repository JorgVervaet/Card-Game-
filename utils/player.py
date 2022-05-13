import random #importing the sample module
from card import Card #importing the Card class from the card.py file

class Player: #here we are making the player
    def __init__(self, player_name):
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []
        self.player_name = player_name
    def play(self):
        card = random.choice(self.cards)
        print("Player: "(self.player_name))+("Turn: "(self.turn_count))
        self.turn_count += 1
        self.history += [card]
        print(self.number_of_cards)
        print(card)
        return card


class Deck:
    def __init__(self):
        self.deck = []
        self.list_of_Player = list_of_Player
        self.number_of_players = number_of_players
       
    def fill_deck(self): #filling the deck with 52 cards
        for i in ["♥", "♦"]: #here we fill only the red cards
            for k in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]:
                self.deck.append(Card ("red", i, k))
        for i in ["♠", "♣"]: #here we fill only the black cards"
            for k in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]:
                self.deck.append(Card ("black", i, k))

       
    def shuffle(self): #shuffling the deck of cards
        z = random.shuffle(self.deck)
        print(z.__str__())
            

    def distribute(self, list_of_Player, number_of_players):
        y = 52 / number_of_players
        for player in players:
            



        
