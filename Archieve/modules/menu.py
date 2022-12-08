def divider(x):
    for i in range(0,x):
        print("-------------------------------------------------------------------------------------")
def greetings():
    # Greetings
    divider(1)
    # main goal
    print("Hello! Fly between airports on your own aircraft!")
    # goal
    print("Your goal is to visit 5 countries as cheaper as possible.")
    # weather
    print("Airports have 20 percent chance to be closed because of bad weather conditions.")
    print("In case you fly to closed airport you get -200cr penalty and stay in current point.")

def commands():
    # List of commands
    divider(1)
    print('Command list:\n"fly": choose destination code and fly\
\n"check": check weather before flight\
\n"info": see list of possible destinations\
\n"status": see list of visited countries and amount of credits remaining\
\n"commands": see list of commands\
\n"exit": finish the game')
    divider(1)

def pictureAircraft1():
    print("      __!__")
    print("^----o-(_)-o----^")
    divider(1)

def messageBadWeather():
    print("The weather is bad and airport is closed. Try again or choose another destination.")

def messageWrong():
    print("Wrong command. Try again.")

def messageStop():
    print("Game stopped.")

def messageReturning():
    print("Returning to choose command...")

def messageNoMoney(playerCredits):
    print("You've run out of credits. Balance is: "+str(playerCredits))