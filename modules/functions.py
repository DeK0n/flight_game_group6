#random weather function
def weather():
    import random
    x=random.randint(0,100)
    # current chance of bad weather is set to 20%
    if x <= 80:
        landing = True
    else:
        landing = False
    return landing

# action draft
def action():
    command = ""
    while command != "exit":
        command = input("Enter command: ")
        if command == "fly":
            print("Enter destination code: ")
        
        elif command == "check":
            print("check")
        elif command == "info":
            print("list of destinations: example code: AA") #change to lists from database
        elif command == "status":
            print("status")
        elif command == "commands":
            print("commands")
        elif command == "exit":
            command = "exit"
            print("Game stopped")
        else:
            print("Wrong command")

