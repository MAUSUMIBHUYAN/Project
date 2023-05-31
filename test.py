<<<<<<< HEAD
=======
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
    
    # function for a single game of blackjack
def blackjack_game(deck):
    #cards for both dealer and player
    player_cards=[]
    dealer_cards=[]
    
    #Scores for both dealer and player
    player_score=[]
    dealer_score=[]
    
    clear()
    
    #initial dealing for player and dealer 
    while len(player_cards)<2:
        #randomly dealing a card
        player_card=random.choice(deck)
        player-cards.append(player_card)
        deck.remove(player_card)
        
        #updating the player score
        player_score+= player_card.card_value
        
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
        
        #randomly dealing a card
        dealer_card= random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        #updating the dealer score
        dealer_score+=dealer_card.card_value

        #print dealer cards and score , keeping in mind to hide the second card and score
        print("DEALER CARDS:")      
        if len(dealer_cards)==1:
              print_cards(dealer_cards,False)
              print("DEALER SCORE=",dealer_score)
        else :
              print_cards(dealer_cards[:-1],True)
              print("DEALER SCORE=",dealer_score-dealer_cards[-1].card_value)

        # in case both the cards are Ace,make the second ace value as 1
        if len(dealer_cards==2)
              if  dealer_cards[0].card_value ==11 and dealer_cards[1].card_value == 11:
                  dealer_cards[1]
        
              
    
    


                






>>>>>>> 6d8e3a08b157c6033d2628b90b34bcbc39ed5e19
