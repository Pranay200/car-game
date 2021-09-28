command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started == True:
            print("Car Already Started.")
        else:
            started = True
            print ("Car started.....")
    elif command == "stop":
        if not started == True:
            print("Car Already Stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
        start - To start the car.
        stop - To stop the car.
        quit - To quit the game.
        """) 
    elif command == "quit":
        break
    else:
        print("Sorry, I can't understand that !")