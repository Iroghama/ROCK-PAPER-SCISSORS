import random
print("Hi! Welcome to the 'ROCK PAPER SCISSORS' game. Just a few rules:\n ROCK beats SCISSORS\n SCISSORS beats paper \n PAPER beats ROCK ")
print("-----------------------------------------------------------------------")
print("In this game:\n R will denote ROCK \n P will deonte PAPER\n S will denote SCISSORS" )
print("-----------------------------------------------------------------------")
print("Your opponent will be the computer.") 
print("-----------------------------------------------------------------------")
print("NOW LET'S PLAY!")
options=['R','P','S']
i=0
while i>=0:
    Computer= random.choice(options)
    Player=input("Enter your option from : R, P or S (make sure it's in uppercase) \n")
    if Player in options: 
        print("Computer","(",Computer,") :","Player","(", Player,")")
        if Computer!= Player:
            if Computer==options[0]:
                #for R
                if Player==options[1]:
                    #for P
                    print("You win!")
                    break
                elif Player==options[2]:
                    #for S
                    print("Computer wins!")
                    break
            elif Computer==options[1]:
                #for P
                if Player==options[0]:
                    #for R
                    print("Computer wins")
                    break
                elif Player==options[2]:
                    #for S
                    print("You win")
                    break   
            elif Computer==options[2]:
                #for S
                if Player==options[0]:
                    #for R
                    print("You win!")
                    break
                elif Player==options[1]:
                    #for P
                    print("Computer wins!") 
                    break 
            else: #not necessary
                pass    
        else:
            print("Oops! looks like it's a Tie. Let's try again")           

    #there should be an else for when both options are the same , print its a tie.
    else:
        #this is where I print error should be at the end of the loop to match my begining if condition. 
        print("Invalid input.")

    i+=1 