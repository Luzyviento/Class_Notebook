# Per the class, we started off with our import and global variables
# that will be utilized by the objects we create to play the game
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
# Here we set the boolean for game play to be used in our while loop
playing = True
# Now we create our classes starting with a card class.
# We need suit and rank attributes
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Then we need a deck class which would take us a bit if we didn't use a for loop or two.
# The class recommends nested for loops and the append method to painlessly build the deck.
# This is the kind of thinking that I still lack.  I don't know when or how to use the tools to which I've already been exposed.
# In order to resolve this problem, I will move a little faster through the lectures and start some of my own projects.
# I do this because I believe that it will force me to bring all of my previously learnt skills to the forefront for analysis.
# I will need a feedback loop of some sort which means it is time for me to find a coding mentor.

class Deck:
# Accepts no arguments as not to allow for deck tampering
    def __init__(self):
        self.deck = []# We start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):# This is just a way to see the the order of the cards in the deck
        deck_comp = ' '
        for card in self.deck:
            deck_comp += ' \n ' + card.__str__()
        return 'the deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)# Here is the shuffle

    def deal(self):
        single_card = self.deck.pop()# This is a 'pop' off the top of the deck embodied in single_card
        return single_card

# Here is some code that we can comment out to test for functionality of our deck objects
# test_deck = Deck() # creates a deck called test_deck
# test_deck.shuffle() # shuffles the test_deck
# print(test_deck) # prints it out for us to see

class Hand:
    def __init__(self):
        self.cards = [] # we start the hand with an empty list just like we did with the deck
        self.value = 0 # We zero the value as we should with most variables
        self.aces = 0 # we add an attribute to allow us to track the aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chips:

    def __init__(self):
        self.total = 100 # we can set this to whatever we want
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips!  You have: {}'.format(chips.total))
            else:
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s ')

        if  x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print("Sorry, I did not understand that.  Please enter h or s only!")
            continue

        break

def show_some(player, dealer):
    print('\nDealer hand:')
    print('<card hidden>')
    print(' ', dealer.cards[1])
    print('\nPlayer hand: ', *player.cards, sep= '\n')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print('bust player')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player wins!!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Player wins.  Dealer busted!!!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer wins!')
    chips.lose_bet()

def push(player, dealer, chips):
    print('Dealer and player tie. Push')

while True:# I'm still having a hard time understanding why
           # so many games start with a while loop when while loops
           # are such a newbie tell per tech media
    # Opening statement
    print("Welcome to BlackJack")
    # create deck instance and shuffle
    deck = Deck()
    deck.shuffle()

    # Set up the player and dealer hands
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the players Chips
    player_chips = Chips()
    # ask for objects
    take_bet(player_chips)
    # Display cards
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    if player_hand.value < 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print('\n Player total chips are at {}'.format(player_chips.total))

    new_game = input('would you like to play again? y/n')

    if new_game[0].lower() == 'y' :
        playing = True
        continue
    else:
        print('Thanks for playing')

        break
