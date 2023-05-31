import random
import os
import time
#defining the card class
class Card:
    def __init__(self,shape,value,Cardvalue):
        # shape of the card 
        self.shape = shape
        # representing value of the card
        self.value = value
        # Cardvalue of the card
        self.Cardvalue = Cardvalue
def clear_terminal():
    os.system("clear terminal")
def print(cards,conceal):
    c = ""
    for i in cards:
        c = c + "\t ________________"
    if conceal:
        c += "\t ________________"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|                |"
    if conceal:
        c += "\t|                |"
    print(c)

    c = ""
    for i in cards:
        if i.value == '10':
            c = c + "\t|   {}               |".format(i.value)
        else:
            c = c + "\t|   {}                |".format(i.value)
    if conceal:
        c += "\t|                |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|                |"  
    if conceal:
        c += "\t|      * *      |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|                |"  
    if conceal:
        c += "\t|     *   *     |"
    print(c)

    c = "" 
    for i in cards:
        c = c + "\t|               |"  
    if conceal:
        c += "\t|    *     *    |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|               |"  
    if conceal:
        c += "\t|   *       *   |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|        {}       |".format(i.shape)
    if conceal:
        c += "\t|           *   |" 
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|               |"
    if conceal:
        c += "\t|          *    |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|               |"
    if conceal:
        c += "\t|         *     |"
    print(c)

    c = "" 
    for i in cards:
        c = c + "\t|               |"
    if conceal:
        c += "\t|               |"
    print(c)

    c = "" 
    for i in cards:
        c = c + "\t|               |"
    if conceal:
        c += "\t|               |"
    print(c)

    c = ""
    for i in cards:
        if i.value == '10':
            c = c + "\t|           {}        |".format(i.value)
        else:
            c = c + "\t|           {}         |".format(i.value)
    if conceal:
        c += "\t|        *       |"
    print(c)

    c = ""
    for i in cards:
        c = c + "\t|________________|"
    if conceal:
        c += "\t|________________|"
    print(c)   
    print()
    
    # creating a function for the blackjack game (single person)
def blackjack_game(deck):
    #cards for both trader and player
    player_cards=[]
    trader_cards=[]
    
    # to write the total Scores for player and trader
    player_score=[]
    trader_score=[]
    
    clear_terminal()
    
    #condition for the trading the card
    while len(player_cards)<2:

        #choosing any card
        player_card=random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
        
        #to update the total scores of the player
        player_score= player_score + player_card.Cardvalue
        
        #in case both the cards are Ace, make the first ace value as 1
        if len(player_cards)==2:
               if player_cards[0].Cardvalue == 11 and player_cards[1].Cardvalue == 11:
                    player_cards[0].Cardvalue=1
                    player_score -= 10
                    
        # print players cards and score
        print("PLAYER CARDS:")
        print_cards(player_cards,False)
        print("PLAYER SCORE=",player_score)
         
        input()
        
        #choosing any card
        trader_card= random.choice(deck)
        trader_cards.append(trader_card)
        deck.remove(trader_card)

        # to update the total scores of the trader
        trader_score= trader_score+trader_card.Cardvalue

        #to print the scores and cards of the trader
        print("TRADER'S CARDS:")      
        if len(trader_cards)==1:
              print_cards(trader_cards,False)
              print("THE TRADER'S SCORE IS=",trader_score)
        else :
              print_cards(trader_cards[:-1],True)
              print("THE TRADER'S SCORE IS=",trader_score-trader_cards[-1].Card_value)

        # in case both the cards are Ace,make the second ace value as 1
        if len(trader_cards==2):
              if  trader_cards[0].Cardvalue ==11 and trader_cards[1].Cardvalue == 11:
                  trader_cards[1].Cardvalue = 1
                  trader_score = trader_score+10

        input()
    #  necessary condition for the player to get blackjack
    if player_score ==21:
        print("PLAYER GOT THE BLACKJACK!!!!") 
        print("PLAYER WINS!!!")
        quit()
    clear_terminal()

    # to print the player and trader cards
    print("TRADER CARDS ARE:")
    print_cards(trader_cards[:-1], True)
    print("TRADER'S SCORE=" , trader_score-trader_cards[-1].Cardvalue)

    print()

    print("PLAYER CARDS ARE:")
    print_cards(player_cards, False)
    print("PLAYER'S SCORE:", player_score)

    #to control the players and traders moves
    while player_score <21:
        option = input("ENTER H for HIT or S for STAND:")

        if len(option)!=1 or (option.upper() != 'H' and option.upper()!= 'S'):
            clear_terminal()
            print ("INVALID INPUT")

        # IF THE PERSON CHOOSES HIT(H)
        if option.upper()== 'H':

            #IF WE HAVE A NEW CARD
            player_card = random.option(deck)
            player_cards.append(player_card)
            deck.remove(player_card)

            #TO ADD UP THE PREVIOUS SCORES
            player_score= player_score+ player_card.Cardvalue

            #IF AT ALL THE PLAYER HAS AN ACE CARD WE NEED TO UPDATE THE PLAYER'S SCORE
            m=0
            while player_score>21 and m<len(player_cards):
                 if player_cards[m].Cardvalue == 11:
                        player_cards[m].cardvalue=1
                       
                        player_score -=10
                        c +=1
                  else:
                        c +=1
             clear_terminal()
            # displaying player and trader cards
            print("TRADER CARDS:")
            print_cards(trader_cards[:-1],True)
            print("TRADER SCORE  = ",trader_score - trader_cards[-1].Cardvalue)
            
            print()
            
            print("PLAYER CARDS:")
            print_cards(player_cards,False)
            print("PLAYER SCORE =",player_score)
            
        # if the player decides to stay and continue
        if option.upper() =='S'
             break
            
      clear_terminal()
      
      
      # PRINT BOTH PLAYER AND TRAER CARDS
        print("PLAYER CARDS:")
        print_cards(player_cards,False)
        print("PLAYER SCORE:",player_score)
        
        print()
        print("TRADER IS GOING TO SHOW HIS CARDS.......:")
        print("TRADER CARDS:")
        
        print_cards(trader_cards,False)
        print("TRADER SCORE=",trader_score)
       # what if the player has a blackjack ....?
        if player_score == 21
            print("PLAYER HAS A BLACKJACK)
            quit()
       # what if the player busts
         if player_score > 21:
             print("PLAYER BUSTED!!! GAME OVERRR!!")
             quit()
                  
          input()
        
       # Managing the trader moves
          while trader_score<17:
               clear_terminal()
               print("TRADER DECIDES TO HIT:")
               
               # Dealing card for trader
                trader_card = random.option(deck)
                trader_cards.append(trader_card)
                deck.remove(trader_card)
               #updating the traders score
                trader_score +=trader_card.Cardvalue
               # Updating player score in case player's card have ace in them
                m =0
                while trader_score >21 and m< len(trader_cards):
                     if trader_cards[m].Cardvalue ==11:
                        trader_cards[m].Cardvalue = 1
                        trader_score -= 10
                        c +=1
                      
                      else:
                         c +=1
                 #PRINT PLAYER NAD TRADER CARDS
                  print("PLAYER CARDS:")
                  print_cards(player_cards,False)
                  print("PLAYER SCORE =",player_score)
                  print()
                  
                  print("TRADER CARDS:")
                  print_cards(trader_cards,False)
                  print("TRADER SCORE =",dealer_score)
                  
                  input()
       # WHAT IF TRADER BUSTS
        if trader_score >21:
                   print("TRADER BUSTED!!! PLAYER WINS!!!)
                   quit()
       # WHAT IF TRADER GETS A BLACKJACK
        if trader_score ==21:
                    print("TRADER WINSS!!! ")
                    quit()
       #TIE
         if trader_score == player_score:
                    print("TIE GAMEE!!!")
       #PLAYER WINSS IF
         if player_score > trader_score:
                     print("PLAYER WINS!!!")
       # TRAER WINS IF
         else:
                     print("TRADER WINS!!!")
         
if __name__ == '__main__':
        # the type of shape
         shape=["Spades","Hearts","Clubs","Diamonds"]
        #the suit value
          suit value ={"Spades":"\u2664","Hearts":"\u2661","Clubs":"\u2667","Diamonds":"\u2662"}
        #the type of card
          cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        # the card values
           Cardvalues={"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
        # the deck of cards
           deck=[]
        # loop for every type of shape
           for shape in shapes:
               # loopfor every type of card in shape
                    for card in shape:
                         #add card to deck
                         deck.append(Card(suits_values[shape],card,cards_values[cards]))

           blackjack_game(deck)

