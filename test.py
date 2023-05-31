
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
    
    clear()
    
    #condition for the trading the card
    while len(player_cards)<2:

        #choosing any card
        player_card=random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
        
        #to update the total scores of the player
        player_score= player_score + player_card.card_value
        
        #in case both the cards are Ace, make the first ace value as 1
        if len(player_cards)==2:
               if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                    player_cards[0].card_value=1
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
        trader_score= trader_score+trader_card.card_value

        #to print the scores and cards of the trader
        print("TRADER'S CARDS:")      
        if len(trader_cards)==1:
              print_cards(trader_cards,False)
              print("THE TRADER'S SCORE IS=",trader_score)
        else :
              print_cards(trader_cards[:-1],True)
              print("THE TRADER'S SCORE IS=",trader_score-trader_cards[-1].card_value)

        # in case both the cards are Ace,make the second ace value as 1
        if len(trader_cards==2)
              if  trader_cards[0].card_value ==11 and trader_cards[1].card_value == 11:
                  trader_cards[1].card_value = 1
                  trader_score = trader_score+10

        input()
    #  necessary condition for the player to get blackjack
    if player_score ==21:
        print("PLAYER GOT THE BLACKJACK!!!!") 
        print("PLAYER WINS!!!")
        quit()
    clear()

    # to print the player and trader cards
    print("TRADER CARDS ARE:")
    print_cards(trader_cards[:-1], True)
    print("TRADER'S SCORE=" , trader_score-trader_cards[-1].card_value)

    print()

    print("PLAYER CARDS ARE:")
    print_cards(player_cards, False)
    print("PLAYER'S SCORE:", player_score)

    #to control the players and traders moves
    while player_score <21:
        option = input("ENTER H for HIT or S for STAND:")

        if len(option)!=1 or (option.upper() != 'H' and option.upper()!= 'S'):
             clear()
             print ("INVALID INPUT")

        # IF THE PERSON CHOOSES HIT(H)
        if option.upper()== 'H':

            #IF WE HAVE A NEW CARD
            player_card = random.option(deck)
            player_cards.append(player_card)
            deck.remove(player_card)

            #TO ADD UP THE PREVIOUS SCORES
            player_score= player_score+ player_card.card_value

            #IF AT ALL THE PLAYER HAS AN ACE CARD WE NEED TO UPDATE THE PLAYER'S SCORE
            m=0
            while player_score>21 and m<len(player_cards):
                 
                                                                   
              
    
    


                




