# Holiday Pokemon Giveaway Game

import random

# Start of the program
def mainMenu():

    print("\n***** Welcome to the Holiday Pokemon Giveaway *****")

    username = input("Please enter your name: ")

    print("")
    print("Hello, " + username + ", good luck, hope you win lots of points!")
    print("\nSelect Game Subject Below:")
    print("1. English \n2. Math \n3. Science \n4. History \n")

    userSubject = input("Enter the number for the subject you want to play in: ")

    while userSubject != "1" or userSubject != "2" or userSubject != "3" or userSubject != "4":
        print("That is not a valid selection, please try again.")

# Matching numbers
def lotteryGame():

    winningNumbers = []

    for num in range(5):
        goalNumber = random.randint(1,20)
        winningNumbers.append(goalNumber)

    for n in range(winningNumbers):
        print(winningNumbers[n])

    
    
# Main Module
def main():

    mainMenu()
    
main()
