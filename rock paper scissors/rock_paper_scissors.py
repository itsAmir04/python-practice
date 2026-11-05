import random as randy
def processRPS(userinput):
    a = randy.randint(-999999 , 999999)
    randy.seed(a)
    computerpick = randy.randint(0,2)
    
    # 0 = rock , 1 = paper , 2 = scissors
     
    #  if userinput = rock

    if userinput == "rock" and computerpick == 0:
        return 'draw'
    elif userinput == "rock" and computerpick == 1:
        return ['oneforcomputer' , userinput , 'paper']
    elif userinput == 'rock' and computerpick== 2:
        return ['oneforuser' , userinput, 'scissors']

    #  if userinput = paper

    elif userinput == 'paper' and computerpick== 0:
        return ['oneforuser' , userinput, 'rock']
    elif userinput == 'paper' and computerpick== 1:
        return 'draw'
    elif userinput == 'paper' and computerpick== 2:
        return ['oneforcomputer' , userinput, 'scissors']
    #  if userinput = scissors

    elif userinput == 'scissors' and computerpick== 0:
        return ['oneforcomputer' , userinput, 'rock']

    elif userinput == 'scissors' and computerpick== 1:
        return ['oneforuser' , userinput, 'paper']

    elif userinput == 'scissors' and computerpick== 2:
        return 'draw'



print(" Hello and welcome to rock paper scissors ".center(100 , '-'))

while True:
    userScore = 0
    computerScore = 0
    starOrnot = input("Shall we start the game?(yes/no)\n")
    if starOrnot=='yes':
        while True:
            if userScore==10 or computerScore == 10:
                if userScore == 10:
                    print(f"You won!!\n My Score :{computerScore}\nYour Score :{userScore}\n")
                    break

                elif computerScore == 10:
                    print(f"I won!!\n My Score :{computerScore}\nYour Score :{userScore}\n")
                    break
            else:
                print("rock paper scissors!!!".center(50,"-"))
                options = ['rock' , 'paper' , 'scissors']
                userpick = input("\nYou picked?\n")
                if userpick not in options:
                    print('\nWRONG INPUT!\n')
                else:
                    result = processRPS(userpick)
                    if result == 'draw':
                        print(f'\nIts a draw\n \n My Score :{computerScore}\nYour Score :{userScore}\n')
                    else:
                        if result[0] == "oneforuser":
                            userScore+=1
                            print(f"\nOne score for you! \n i picked {result[2]} and you picked {result[1]} \n \nMy Score :{computerScore}\nYour Score :{userScore}\n ")
                            continue
                        elif result[0] == "oneforcomputer":
                            computerScore+=1
                            print(f"\nOne score for me! \n i picked {result[2]} and you picked {result[1]} \n \nMy Score :{computerScore}\nYour Score :{userScore}\n ")
                            continue

    elif starOrnot =='no':
        print('\nOk have a great day')
        break
    else:
        print('\nWRONG INPUT!')
