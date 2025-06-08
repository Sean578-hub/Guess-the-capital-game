#      Q05

gusse = 0
score = 0
questionCount = 0
name = None
def displayMenu():
    global score
    global name
    # Completed subprogram that displays the menu

    print("                  Menu                    ")
    print("------------------------------------------")
    print("[1] Add player name")
    print("[2] Play guess the capital city")
    print("[3] End game")
    print("------------------------------------------")


def getMenuChoice():
    # Completed subprogram that gets and validates the menu choice
    choices = [1, 2, 3]
    mChoice = 0

    # Menu choice is validated
    while mChoice not in choices:
        mChoice = int(input("Input your menu choice: "))

    # Valid menu option returned to the main menu
        if mChoice == 1:
            addPlayerName()
        elif mChoice == 2:
            guessCapital()
        elif mChoice == 3:
            print(f"Name: {name}")
            print(f"score: {score}")
            return mChoice


def addPlayerName():
    global name

# Add your code to:
#   ensure a player name is input
#   return the player name to the main menu
    name = input("Enter your name ")

    return name


def guessCapital():
    global questionCount
    global gusse
    global score
    # Partially completed subprogram to:
    #   display questions
    print("Here are the questions")
    print("--------------------------------------------------------")
    print("1. What is the capital city of England? ")
    print("2. What is the capital city of France? ")
    print("3. What is the capital city of Spain? ")
    print("4. What is the capital city of Italy? ")
    print("5. What is the capital city of Germany? ")
    print("6. What is the capital city of Scotland? ")
    print("7. What is the capital city of Wales? ")
    print("8. What is the capital city of United Arab Emirates? ")
    print("9. What is the capital city of China? ")
    print("--------------------------------------------------------")

    while questionCount !=5:
        choice = int(input("Enter the nambers 1 to 9 to chose which question you would want to answer "))
        while choice <1 or choice >9:
            print("Error")
            choice = int(input("Enter the nambers 1 to 9 to chose which question you would want to answer "))

        if choice == 1:
            q1 = input("1. What is the capital city of England? ")
            if q1 == "London":
                gusse +=1
                score +=1
                questionCount += 1
            else:
                gusse +=1
                questionCount +=1

        elif choice == 2:
            q2 = input("2. What is the capital city of France? ")
            if q2 == "Paris":
                gusse +=1
                score +=1
                questionCount += 1
            else:
                gusse +=1
                questionCount += 1

        elif choice == 3:
            q3 = input("3. What is the capital city of Spain? ")
            if q3 == "Madrid":
                gusse +=1
                score +=1
                questionCount += 1
            else:
                gusse +=1
                questionCount += 1

        elif choice == 4:
            q4 = input("4. What is the capital city of Italy? ")
            if q4 == "Rome":
                gusse +=1
                score +=1
                questionCount += 1
            else:
                gusse +=1
                questionCount += 1

        elif choice == 5:
            q5 = input("5. What is the capital city of Germany? ")
            if q5 == "Berlin":
                gusse +=1
                score +=1
                questionCount += 1
            else:
                gusse +=1
                questionCount += 1

        elif choice == 6:
            q6 = input("6. What is the capital city of Scotland? ")
            if q6 == "Edinburgh":
                gusse +=1
                score +=1
                questionCount += 1
            else:
                gusse +=1
                questionCount += 1

        elif choice == 7:
            q7 = input("7. What is the capital city of Wales? ")
            if q7 == "Cardiff":
                gusse +=1
                score +=1
                questionCount += 1
            else:
                gusse +=1
                questionCount += 1

        elif choice == 8:
            q8 = input("8. What is the capital city of United Arab Emirates? ")
            if q8 == "Abu Dhabi":
                gusse +=1
                score +=1
                questionCount += 1
            else:
                gusse +=1
                questionCount += 1

        elif choice == 9:
            q9 = input("9. What is the capital city of China? ")
            if q9 == "Beijing":
                gusse +=1
                score +=1
                questionCount += 1
            else:
                gusse +=1
                questionCount += 1

    #   check guesses
    print(f"Your number of guesses are: {gusse}")
    #   return final score
    print(f"Your score is: {score}")

    # Arrays holding question numbers, countries and their capital cities
    questions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    countries = ["England", "France", "Spain", "Italy", "Germany", "Scotland", "Wales", "United Arab Emirates", "China"]
    capitals = ["London", "Paris", "Madrid", "Rome", "Berlin", "Edinburgh", "Cardiff", "Abu Dhabi", "Beijing"]

    questionCount = 1
    questionScore = 0

    # Add your code here

    return


menuChoice = 0
score = 0
playerName = ""

while menuChoice != 3:
    displayMenu()
    menuChoice = getMenuChoice()

