command = input("Enter command: ")
while command != "quit":
    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to quit")