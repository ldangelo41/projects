import os
import random   #allows the program to pick a random number in specified range
import operator     #allows program to use operator commands
import time

#function for greetings the user
def greetings():
    print("Welcome to this math game!\
    \nThis game is meant to enhance your math skills!\
    \nTo win or score the highest, you need to be quick!\
    \nMake sure you stay focused, and enjoy the game")

    #printing instruction
    input("To start, press enter . . .")
    clear_screen()
    print("There is 3 different difficulties you can choose from\
    \nEasy, Medium, and Hard\
    \nThe harder the difficulty, the more points you can score\
    \nAgain, focus and try be fast to answer as many questions as you can\
    \nin the time given.\n")

#printing list of options to choose from
def listOfOptions():
    print("Enter 1 to Play Easy\
    \nEnter 2 to Play Medium\
    \nEnter 3 to Play Hard\
    \nEnter 4 to Quit the game and/or View scores")

#function to clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#Function that get the name from the user
def getName ():
    # This is where the user will enter their name
    name = input("Please enter your name: ")
    name = name.title()
    clear_screen()
    #We will have a couple of print statements that are responsible for engaging & directing the user.
    print("Hello " + name + "!")
    print("Again, welcome to this math game!\
    \nNow " + name + " you must select the level of difficulty you want.")
    input ("Press enter to continue . . .")
    clear_screen()

    return name

#Easy problem generators (only addition)
def probFinderEasy():
    #possible operators
    ops = {'+':operator.add}
    num1 = random.randint(1,10)
    num2 = random.randint(1,20)
    operation = random.choice(list(ops.keys()))

    answer = ops.get(operation)(num1, num2)

    print('{} {} {}: '.format(num1, operation, num2))

    return answer

#Mid problem generators (add and sub)
def probFinderMid():
    ops = {'+':operator.add,
           '-':operator.sub}    #possible operators
    num1 = random.randint(1,50)
    num2 = random.randint(1,30)
    if num2 > num1:
        num2, num1 = num1, num2
    operation = random.choice(list(ops.keys()))
    answer = ops.get(operation)(num1, num2)
    print('{} {} {}: '.format(num1, operation, num2))
    return answer

#Hart problem generators (add, sub, and multi)
def probFinderHard():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul}    #possible operators
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    operation = random.choice(list(ops.keys()))
    answer = ops.get(operation)(num1, num2)
    print('{} {} {}: '.format(num1, operation, num2))
    return answer

#calls the generators and take users answer (Easy)
def questionEasy():
    answer = probFinderEasy()
    guess = float(input("Your answer: "))
    return guess == answer

#calls the generators and take users answer (Mid)
def questionMid():
    answer = probFinderMid()
    guess = float(input("Your answer: "))
    return guess == answer

#calls the generators and take users answer (Hard)
def questionHard():
    answer = probFinderHard()
    guess = float(input("Your answer: "))
    return guess == answer


#main game
def main():

    greetings() #greeting the user and clearing the screen
    name = getName()
    listOfOptions() #giving the user options to choose which level they would like to play
    userEntry = input("\nYour entery: ") #taking the user input to start the game or quit
    score, right, wrong = 0, 0, 0 #declaring some variables

    #starting the big while loop (the game itself)
    while userEntry != 4:
        #entering easy mode
        if userEntry == '1':
            timeEnd = time.time() + 75 * 1
            print("\nGood choice!\nLevel Easy consist of addition questions only")
            print("You have 60 seconds to answer as many questions as you can")
            input ("Press enter to start . . .")
            clear_screen()
            score = 0
            right = 0
            wrong = 0
            while time.time() < timeEnd:
                correct = questionEasy()
                if correct:
                    score = score + 1
                    right = right + 1
                else:
                    wrong = wrong + 1
            #random score creater in the range of 80 and 100 since it is easy
            score = score * random.randint(80,100)

            print("\nYou got " + str(right) +" correct answeres")
            print("You got " + str(wrong) +" wrong answeres")
            print("You score was " + str(score) + "\n")

        elif userEntry == '2':
            timeEnd = time.time() + 75 * 1
            print("\nGood choice!\nThis level consist of addition and subtraction questions only\
                    \nThere is no negative values for any of the questions")
            print("You have 60 seconds to answer as many questions as you can")
            input ("Press enter to start . . .")
            clear_screen()

            score = 0
            right = 0
            wrong = 0
            while time.time() < timeEnd:
                correct = questionMid()
                if correct:
                    score = score + 1
                    right = right + 1
                else:
                    wrong = wrong + 1
            #random score creater in the range of 100 and 129 since it is easy
            score = score * random.randint(100,129)

            print("\nYou got " + str(right) +" correct answeres")
            print("You got " + str(wrong) +" wrong answeres")
            print("You score was " + str(score) + "\n")

        elif userEntry == '3':
            timeEnd = time.time() + 75 * 1
            print("\nYou look like you like a challenge!\nThis level consist of addition, subtraction and multiplication questions\
                    \nThere is negative values for substraction questions\
                    \nbut hey, you can earn more points, just be quick and focus!")
            print("You have 60 seconds to answer as many questions as you can")
            input ("Press enter to start . . .")

            clear_screen()
            score = 0
            right = 0
            wrong = 0
            while time.time() < timeEnd:
                correct = questionHard()
                if correct:
                    score = score + 1
                    right = right + 1
                else:
                    wrong = wrong + 1
            #random score creater in the range of 100 and 129 since it is easy
            score = score * random.randint(130,150)

            print("\nYou got " + str(right) +" correct answeres")
            print("You got " + str(wrong) +" wrong answeres")
            print("You score was " + str(score) + "\n")

        elif userEntry == '4':
            print("You choose to quit and/or view scores")
            break

        else: #error or invalid user entery
            print("That was an invalid input\
            \nPlease choose from the following optinos. \n")

        input ("Press enter to continue . . .")

        clear_screen()
        listOfOptions()
        userEntry = input("\nYour entery: ")

    question = input("Do you want to add your score to our highscores list before you leave\
                    \nOr you just would like to quit the game [yes/no]: ")
    question = question.title()
    clear_screen()
    while True:
        if question == 'Yes':
            file = open ('nameAndScore.txt', 'a')
            user = name
            #insert in list the score following by the name
            with open ('nameAndScore.txt', 'a') as f:
                record = (user.title() + "," + " " + str(score) + "\n")
                f.write(record)

            #filling the scores list with scores and names
            scores = open ('nameAndScore.txt').read().splitlines()

            #sort list of scores by score
            output = []
            for entry in scores:
                values = entry.split(',')
                output.append([values[0], sorted([int(x) for x in values[1:]], reverse=True)])

            scores = ['{}, {}'.format(entry[0], ','.join(str(x) for x in entry[1])) for entry in sorted(output, key=lambda x: x[1], reverse=True)]
            print("Highest five scores are: \n")
            i = 0
            for topfive in range(5):
                i = i + 1
                print(str(i) + ": " + scores[topfive])

            #print the whole list sorted
            print("")

            record = user.title() + "," + " " + str(score)
            yourRank = scores.index(record)
            print("You rank is: " + str(yourRank+1))

            if str(yourRank+1) == '1':
                print("Congradulation " + name + ", you broke the highest score recorded")
            print("Thank you for playing!\
                \nBetter Luck next time!")
            break
        elif question == 'No':
            print("Thank you for playing!\
                \nBetter Luck next time!")
            break
        else:
            print("Invalid entry!")
            question = input("Do you want to add your score to our highscores list before you leave\
                    \nOr you just would like to quit the game [yes/no]: ")
            question = question.title()
            clear_screen()
main()