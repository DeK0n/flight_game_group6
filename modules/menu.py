def divider():
    print("-------------------------------------------------------------------------------------")
def greetings():
    # Greetings
    divider()
    # main goal
    print("Hello! Fly between airports on your own aircraft!")
    # goal
    print("Your goal is to visit 5 countries with lowest budjet.")
    # weather
    print("Airports have 20 percent chance to be closed because of bad weather.")
    print("In case you fly to closed airport you get -200cr penalty and stay in current point.")

def commands():
    # List of commands
    divider()
    print('Command list:\n"fly": choose destination code and fly\
\n"check": check weather before flight\
\n"info": see list of possible destinations\
\n"status": see list of visited countries and amount of credits remaining\
\n"commands": see list of commands')
    divider()

def pictureAircraft1():
    print("      __!__")
    print("^----o-(_)-o----^")
    divider()

def messageBadWeather():
    print("The weather is bad and airport is closed. Try again or another destination.")

def messageWrong():
    print("Wrong command. Try again.")

def messageStop():
    print("Game stopped")

def messageReturning():
    print("Retruning to choose command...")

def messageNoMoney(playerCredits):
    print("You ran out of credits. Balance is: "+str(playerCredits))