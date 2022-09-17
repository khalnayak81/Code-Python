#car game.
command = ""
started = False
while True :
    command = input("> ").lower()
    if command == "start":
        if started :
            print("car is already started.")
        else:
            started = True    
            print('the car is started')
    elif command == "stop":
        if not started :
            print('the car is already stoped')
        else:
            started = False    
            print('the car is stoped')
    elif command == "help":
        print("""
start--- to start car
stop--- to stop car
quit--- to quit the game""")
    elif command == "quit":
        break             
    else:
        print("Sorry I don't understand.")
        
        