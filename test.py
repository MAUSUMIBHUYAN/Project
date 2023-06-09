import random

shapes = ('Spades','Diamonds','Hearts','Clubs')
ranks = ('2','3','4','5','6','7','8','9','Ace','Jack','Queen','King')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7':7, '8':8, '9':9, 'Ace':11, 'Jack':11, 'Queen':12, 'King':13, }

#when the game is playing properly not the whole loop that makes the whole game
playing = True
#define Classes
class Cards: #creates all the cards
    def __init__(self,shape,rank):#to add attributes
        self.shape = shape
        self.rank = rank
    def __str__(self):
        symbols = {
            'Spades': '♠',
            'Diamonds': '♦',
            'Hearts': '♥',
            'Clubs': '♣'
        }
        rank_symbols = {
            '2':'2',
            '3':'3',
            '4':'4',
            '5':'5',
            '6':'6',
            '7':'7',
            '8':'8',
            '9':'9',
            '10':'10',
            'Ace':'A',
            'Jack':'J',
            'Queen':'Q',
            'King':'K'
        } 
        card_art = [

            '┌─────────┐',
             f'│ {rank_symbols[self.rank]:<2}      │',
             '│         │',
             f'│    {symbols[self.shape]:<1}    │',
             '│         │',
             f'│      {rank_symbols[self.rank]:>2} │',
             '└─────────┘'
        ]
        
        return '\n'.join(card_art)
class Deck:#create a deck of cards
    def __init__(self):
        self.deck = [] # haven't created a deck
        for shape in shapes:
            for rank in ranks:
                self.deck.append(Cards(shape,rank))#to create a nice stack and all deck is going to be like a whole string

    def __str__(self):
        combination_of_deck = ''
        for card in self.deck:
            combination_of_deck += '\n' + card.__str__()#my combination of deck is equal to my deck which can't plus the card so a new line and a card is equal to deckcomination and setting the value again so reassigning it every time
        return 'The deck has : ' +combination_of_deck

    def shuffle(self): #shuffles the card in the deck
        random.shuffle(self.deck)

    def pick(self): #pick the card from the deck
        #pop means takeoff the lastvalue from a list or a string        
        pickout_card = self.deck.pop()#the pickout card is going to be the card that is popped off from the end of the deck
        return pickout_card


class Have: #shows all the cards that the player and the opponent have 
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def add_card(self, card): #add a card to the player as well as the opponent
        self.cards.append(card)
        self.value += values[card.rank] #calculating the values of the cards
    
class Bets: # to keep track of all the bets 
    def __init__(self):
        #when the user lost their bet,the amount they bet was taken away from the self.total
        self.total = 0
        self.bet = 0

    def win_the_bet(self):
        self.total += self.bet

    def lost_the_bet(self):
        self.total -= self.bet
#functions
def take_the_bet(amount):

    while True:
        try:
            amount.bet = int(input("Enter the amount you want to bet:"))
        except ValueError:
            print("Excuse me! Can you type in a number:")
        else:
            if amount.bet < 100:
                print("Your bet should not be less than 100!") 
            else:
                break
def hit(deck, have):
    have.add_card(deck.pick())

def hit_or_stand(deck, have):
    global playing#making it available  in the function

    while True:
        ask = input("Would you like to hit or stand: ")

        if ask.lower() == 'hit':
            hit(deck, have)
        elif ask.lower() == 'stand':
            print("Player choose to stand, the ooponent start playing.")
            playing = False#it won't stop the whole loop of the game but it will stop the player from doing anything else while the dealer is playing
        else:
            print("you can either type hit or stand.")
            continue
        break#it will break if the answer is correct

def show_the_card(player, opponent):
    print("\nOpponent have: ")
    print("card is hidden")
    print(opponent.cards[1])
    print("\nplayer has: ")#separate the cards together and separate it with new line
    for i ,card in enumerate(player.cards, start=1):
        print("card {}{}".format(str(i)+':'+'\n',card))

def show_card(player, opponent):
    print("\nOpponent have: ")
    for i ,card in enumerate(opponent.cards, start=1):
        print("card {}{}".format(str(i)+':'+'\n',card))
    print("Opponent total value:",opponent.value)
        

    print("\nPlayer has:")
    for i ,card in enumerate(player.cards, start=1):
        print("card {}{}".format(str(i)+':'+'\n',card))
    print("Player total value:", player.value)

#game endings
def player_lose(player, opponent, amount):
    print("OHH,YOU LOST THE GAME!")
    print("Player total value:", player.value)
    print("Opponent total value:", opponent.value)
    amount.lost_the_bet()
def player_win(player, opponent, amount):
    print("BRAVO,YOU WON THE GAME!")
    amount.win_the_bet()
def opponent_lose(player, opponent, amount):
    print("BRAVO,OPPONENT LOST THE GAME!")
    amount.win_the_bet()
def opponent_win(player, opponent, amount):
    print("OHH,OPPONENT WON THE GAME!")
    print("Player total value:", player.value)
    print("Opponent total value:", opponent.value)
    amount.lost_the_bet()

def Tie(player, opponent):#if the player and the opponent tie
    print("Its a tie!")

#build the game
while True:
    print("Welcome to Blackjack game!")

    #create an shuffle deck
    deck = Deck()
    deck.shuffle()

    player_have = Have()
    player_have.add_card(deck.pick())#add the card twice
    player_have.add_card(deck.pick())

    opponent_have = Have()
    opponent_have.add_card(deck.pick())#add the card twice
    opponent_have.add_card(deck.pick())

    #set up the amount
    player_bet = Bets()

    #ask player for bet
    take_the_bet(player_bet)
    #show cards
    show_the_card(player_have, opponent_have)
    
    while playing:
        hit_or_stand(deck, player_have)
        show_the_card(player_have, opponent_have)

        if player_have.value > 21:
            player_lose(player_have, opponent_have, player_bet)
            break
    if player_have.value <= 21:
        while opponent_have.value < 17:
            hit(deck, opponent_have)
        show_card(player_have, opponent_have)     
        if opponent_have.value > 21:
            opponent_lose(player_have , opponent_have, player_bet)       
        elif player_have.value > opponent_have.value:
            player_win(player_have, opponent_have, player_bet)
        elif player_have.value < opponent_have.value:
            opponent_win(player_have, opponent_have, player_bet)
        else:
            Tie(player_have, opponent_have)    
    
    print("\nPlayer's winnings stand at", player_bet.total)
    #show the hidden card
    print("\nHidden card of the opponent:")
    print(opponent_have.cards[0])

    new_game = input("Would you like to play again?")
    if new_game.lower() == 'yes':
        playing = True
        continue
    else:
        print("Thanks for playing the Blackjack game!")
        break
