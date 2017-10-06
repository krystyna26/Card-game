#Group Activity
from random import shuffle
class card(object):
    def __init__(self, suit, number):
        self.number = number
        if suit == 1:
            self.suit = 'Spade'
        elif suit == 2:
            self.suit = 'Heart'
        elif suit == 3:
            self.suit = 'Club'
        elif suit == 4:
            self.suit = 'Diamond'
        
class Deck(object):
    def __init__(self):
        self.deck = []  #this holds a list of carsd in the deck, so now we need methods to make the deck (52 cards), we can define the cards by number 1-13
    def makeDeck(self):
        # card =(number, suit) <-- tupple
        #for i in range(1,53):

        for number in range(1,14):
            for suit in range(1,5):
                i = card(suit, number)
                self.deck.append(i)

    def shuffle(self):
        shuffle(self.deck) 

    def printDeck(self):
        for data in self.deck:
            print 'card:',data.number,
            print 'suit:',data.suit

class Player(object):
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.deck.pop())

    def throwCard(self):
        self.hand.pop()

    def showCard(self):
        print 'These cards in hand:'
        for data in self.hand:
            print data.number,
            print data.suit
        

deck1 = Deck()
deck1.makeDeck()
#deck1.printDeck()
deck1.shuffle()
player1 = Player('Bob')
player1.draw(deck1)
player1.draw(deck1)
player1.draw(deck1)
player1.showCard()
player1.throwCard()
player1.showCard()

#deck1.printDeck()

#these are the memory address holding the 52 i, let me figure out how to print the actual thing
# i am just testing if we can call deck1 from inside the player class     
#so we made i range from 1 to 52, and each i represent a unique card
#each 'i' will have a number from 1-13
#and each i will have a number from 1 to 4
#since each i have a unique number and unique suit, we can append 52 of the 'i's to the deck
#so after running makeDeck(), self.deck will have 52 'i's
#lets try it


#lets ask if we are going to right directionclear
#the 1,2,3,4 is the type

#so now we need to make a player class, with method draw, so when we draw, we delete a card ffrom deck, but add that card to p;ayer's hand
#do you think Anna needs to see jack,queen, king, and A.. just want to make sure..
#i think we can just add it later for time 
#let's work on PLAYER!!