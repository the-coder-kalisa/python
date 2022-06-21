command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "quit":
        print("Bye")
        break
    elif command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to quit")
    else:
        print("Sorry, I don't understand that command. Please use help to see all commands")