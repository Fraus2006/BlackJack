# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


import random


class Card:
    def __init__(self,name,value):
        self.name=name
        self.value=value
        

two=Card("two",2)
three=Card("three",3)
four=Card("four",4)
five=Card("five",5)
six=Card("six",6)
seven=Card("seven",7)
eight=Card("eight",8)
nine=Card("ninee",9)
ten=Card("ten",10)
jack=Card("jack",10)
queen=Card("queen",10)
king=Card("king",10)
ace=Card("Ace",12) 

deck=[two,two,two,two,three,three,three,three,four,four,four,four,five,five,five,five,
six,six,six,six,seven,seven,seven,seven,eight,eight,eight,eight,nine,nine,nine,nine,
ten,ten,ten,ten,jack,jack,jack,jack,queen,queen,queen,queen,king,king,king,king,ace,ace,ace,ace]


#computers turn = "C" and players turn = "P"
oppositeTurn= "k"
chosenCard=0
totalValueOfCards=0
playersCards= []
totalValueOfCardsOfComputer=0
gameStatus = "ingame"
#Hit 
#Deciding if ace is 1 or 11
#adding cards to the players deck, so he knows, whitch cards he has.
def hit():
    global oppositeTurn
    global chosenCard
    i = random.randint(0,len(deck))
    chosenCard=deck[i]
    deck.pop(i)
    
    if oppositeTurn =="C" and chosenCard.value ==12:
        decide = int(input("Chose the value of your Ace by tiping 1 or 11\n"))
        if decide ==1 :
            chosenCard.value =1
        elif decide == 11:
            chosenCard.value=11
        else:
            hit()
    elif  chosenCard.value ==12 and  totalValueOfCardsOfComputer >=11:
        chosenCard.value =1
    elif  chosenCard.value ==12 and  totalValueOfCardsOfComputer <11:
        chosenCard.value =11

    else:   
        pass
    
    if oppositeTurn == "C":
        playersCards.append(chosenCard.name)
        playersCards.append(chosenCard.value)
    else:
        pass

#complete player turn 
def playerTurn():
    global oppositeTurn
    oppositeTurn = "C"
    global gameStatus
    
    stayOrHit = input("Chose to Stay or Hit by tiping 1(Stay) or 2(Hit) \n")
    if stayOrHit== "1":
        gameStatus = "End"
        lose()
        winn()
        computerTurn()
    elif stayOrHit== "2":
        hit()
        global totalValueOfCards
        totalValueOfCards+=chosenCard.value
        print(f"Your total value of cards is {totalValueOfCards}")
        print(f"You have theese cards {playersCards} \n")
        print()
        
        lose()
        winn()
        computerTurn()
    else:
        print("Try it again")
        print()
        playerTurn()
    
    pass

#complete computer turn
def computerTurn():
    print("Now it is Computers turn")
    global oppositeTurn
    oppositeTurn = "P"
    global totalValueOfCardsOfComputer
    global gameStatus
    
    if totalValueOfCardsOfComputer <=11:
        hit()        
        totalValueOfCardsOfComputer+=chosenCard.value
        print("Computer chosed to hit.")
        print()
        print()
        lose()
        winn()
        playerTurn()
    elif totalValueOfCardsOfComputer >=14 and totalValueOfCardsOfComputer <16 :
        luckyRoll= random.randint(1,2)
        if luckyRoll ==1:
            hit()        
            totalValueOfCardsOfComputer+=chosenCard.value
            print("Computer chosed to hit.")
            print()
            print()
            lose()
            winn()
            playerTurn()
        else:
            print("Computer chosed to stay")
            gameStatus = "End"
            lose()
            winn()
    elif totalValueOfCardsOfComputer >=16 <=19:
        luckyRoll2= random.randint(1,4)
        if luckyRoll2 ==1:
            hit()        
            totalValueOfCardsOfComputer+=chosenCard.value
            print("Computer chosed to hit.")
            print()
            print()
            lose()
            winn()
            playerTurn()
        else:
            print("Computer chosed to stay")
            gameStatus = "End"
            lose()
            winn()
            
    elif totalValueOfCardsOfComputer ==21:
        print("Computer chosed to stay")
        gameStatus = "End"
        lose()
        winn()
        
    elif totalValueOfCardsOfComputer >11 and totalValueOfCardsOfComputer <14:
        print("Computer chosed to stay")
        gameStatus = "End"
        lose()
        winn()
    else:
        pass






def winn():
    global totalValueOfCardsOfComputer
    if oppositeTurn == "P":
        if totalValueOfCardsOfComputer > totalValueOfCards and totalValueOfCardsOfComputer <=21 and gameStatus != "ingame":
            print(f"Computer scored {totalValueOfCardsOfComputer}.")
            print("Computer had won, better luck next time.")
            playAgain()
        else:
            pass
    else:
        if totalValueOfCards > totalValueOfCardsOfComputer and  totalValueOfCards <=21 and gameStatus != "ingame":
            print(f"You have {totalValueOfCards} and computer have {totalValueOfCardsOfComputer}.")
            print("You had won, congratulations. You have more than Computer")
            
            playAgain()


def lose():
    if oppositeTurn == "P":
        if totalValueOfCardsOfComputer >21:
            print(f"Total value of cards of computer is {totalValueOfCardsOfComputer}.")
            print("Computer had lost, he has over 21")
            playAgain()
        elif gameStatus !="ingame" and totalValueOfCardsOfComputer < totalValueOfCards:
            print(f"You have {totalValueOfCards} and computer have {totalValueOfCardsOfComputer}.")
            print("Computer had lost, you are closer to  21")
            playAgain()
        else:
            pass
    else:
        if totalValueOfCards >21:
            print(f"You have {totalValueOfCards} and computer have {totalValueOfCardsOfComputer}.")
            print("You had lost, you have over 21")
            playAgain()
        elif gameStatus !="ingame" and totalValueOfCards < totalValueOfCardsOfComputer:
            print(f"You have {totalValueOfCards} and computer have {totalValueOfCardsOfComputer}.")
            print("You had lost, Computer is closer to  21")
            playAgain()
        else:
            pass



def playAgain():
    global totalValueOfCards
    totalValueOfCards = 0
    global totalValueOfCardsOfComputer
    totalValueOfCardsOfComputer =0
    playersCards = []
    
    decide = input("Press A for playing Again and S for Stop playing. \n")
    if decide == "s" or decide == "S":
        exit()
    elif decide == "a" or decide == "A":
        playerTurn()
    else:
        playAgain()
        
playerTurn()