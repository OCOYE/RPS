from random import choice

tools = [
    "Rock", "Paper", "Scissors"
]

# Welcome, player!
print(""" _______                   __       _______                                ______           _                                       
|_   __ \                 [  |  _  |_   __ \                             .' ____ \         (_)                                      
  | |__) |   .--.   .---.  | | / ]   | |__) |,--.  _ .--.   .---.  _ .--.| (___ \_| .---.  __   .--.   .--.   .--.   _ .--.  .--.   
  |  __ /  / .'`\ \/ /'`\] | '' <    |  ___/`'_\ :[ '/'`\ \/ /__\\[ `/'`\]_.____`. / /'`\][  | ( (`\] ( (`\]/ .'`\ \[ `/'`\]( (`\]  
 _| |  \ \_| \__. || \__.  | |`\ \  _| |_   // | |,| \__/ || \__., | |   | \____) || \__.  | |  `'.'.  `'.'.| \__. | | |     `'.'.  
|____| |___|'.__.' '.___.'[__|  \_]|_____|  \'-;__/| ;.__/  '.__.'[___]   \______.''.___.'[___][\__) )[\__) )'.__.' [___]   [\__) ) 
                                                  [__|                                                                              """)
print("\nType 'Close' to close the software!\n")

# Game
while True:
    tochoice = input("Choice [Rock, Paper and Scissors]:\n").strip().capitalize()
    computerchoice = choice(tools)
    if tochoice == "Close":
        print("Closing...")
        break
    elif tochoice == "Rock" and computerchoice == "Rock":
        print(f"Tie!! Try again! Computer chose: {computerchoice}")
    elif tochoice == "Rock" and computerchoice == "Paper":
        print(f"Computer chose: {computerchoice}! Haha, try again!")
    elif tochoice == "Rock" and computerchoice == "Scissors":
        print(f"You won! Your computer wants to try again. Computer chose: {computerchoice}")
    elif tochoice == "Paper" and computerchoice == "Paper":
        print(f"Tie!!!!!!!! Computer chose: {computerchoice}")
    elif tochoice == "Paper" and computerchoice == "Rock":
        print(f"You won! Computer chose: {computerchoice}")
    elif tochoice == "Paper" and computerchoice == "Scissors":
        print(f"Computer won! Computer chose: {computerchoice}")
    elif tochoice == "Scissors" and computerchoice == "Scissors":
        print(f"Bro... Tie! Computer chose: {computerchoice}")
    elif tochoice == "Scissors" and computerchoice == "Paper":
        print(f"You won! Congratulations! Computer chose: {computerchoice}")
    elif tochoice == "Scissors" and computerchoice == "Rock":
        print(f"Computer won! Computer chose: {computerchoice}, Try Again!")
    else:
        print("Error! Try Again!")