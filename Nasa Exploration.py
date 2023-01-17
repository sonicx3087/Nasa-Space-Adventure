import time


def intro():
    print("Welcome to NASA Space Adventure!")
    print(
        "You are the commander of the USS Enterprise, a new state-of-the-art spacecraft on a mission to explore a distant planet.")
    print("As you approach the planet, you realize that there is a problem with your ship.")
    print("You need to make some quick decisions to fix the ship and continue your mission.")
    print("Let's begin...")
    print()
    time.sleep(2)


def decision1():
    print("As you inspect the ship, you notice that the fuel tank is leaking.")
    print("You need to decide how to fix the leak.")
    print("1. Use duct tape to patch the leak.")
    print("2. Use the ship's spare parts to repair the fuel tank.")
    print("3. Signal for help to the nearest space station.")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You use duct tape to patch the leak.")
        print("The leak is temporarily fixed, but the duct tape may not hold for long.")
        print("You will need to find a more permanent solution soon.")
        print()
        time.sleep(2)
    elif choice == 2:
        print("You use the ship's spare parts to repair the fuel tank.")
        print("The fuel tank is now repaired and the leak is fixed.")
        print()
        time.sleep(2)
    elif choice == 3:
        print("You signal for help to the nearest space station.")
        print("A rescue team arrives and helps you repair the fuel tank.")
        print("You are now ready to continue your mission.")
        print()
        time.sleep(2)


def decision2():
    print("As you continue your mission, you come across a strange object in space.")
    print("You need to decide how to approach the object.")
    print("1. Ignore the object and continue your mission.")
    print("2. Investigate the object.")
    print("3. Send a drone to investigate the object.")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You ignore the object and continue your mission.")
        print("You may never know what the object was.")
        print()
        time.sleep(2)
    elif choice == 2:
        print("You investigate the object.")
        print("As you get closer, you realize that it is a long lost space station.")
        print("You dock your ship at the station and find valuable resources.")
        print("This will help you complete your mission successfully.")
        print()
        time.sleep(2)
    elif choice == 3:
        print("You send a drone to investigate the object.")
        print("The drone returns with valuable information about the object.")
        print("Based on the drone's data, you decide to investigate the object further.")
        print()
        time.sleep(2)


def decision3():
    print("As you approach the planet, you encounter a dangerous storm.")
    print("You need to decide how to navigate through the storm.")
    print("1. Attempt to fly through the storm.")
    print("2. Attempt to fly around the storm.")
    print()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You attempt to fly through the storm.")
        print("Your ship is hit by lightning and your mission is a failure.")
        print()
        time.sleep(2)
    elif choice == 2:
        print("You attempt to fly around the storm.")
        print("You successfully navigate around the storm and land safely on the planet.")
        print("Congratulations! You have completed your mission!")
        print()
        time.sleep(2)

def end():
    print("Thank you for playing NASA Space Adventure!")
    print("We hope you had fun and learned a little bit about space exploration.")

intro()
decision1()
decision2()
decision3()
end()