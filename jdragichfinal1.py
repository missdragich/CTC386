#JDragich final program 1
print("Menu")
print("------------------------------------------")
print("Option 1 - Joke")
print("Option 2 - Food")
print("Option 3 - Guessing Game")
print("------------------------------------------")
print("Which option would you like to choose?")
option = int(input(">"))
if (option == 1):
    print("Hello, friend! Say, what's your name?")
    name = input(">")
    print(name, "? Like the serial killer?")
    print("OK, I guess that one is funnier if you say it after someone tells you their baby's name.")
if (option == 2):
    print("Hey, friend! What is your favorite food?")
    food = input(">")
    for i in range(20):
        print(food)
elif (option == 3):
    x = int(input("Guess a whole number."))
    while (x !=0):
        x = int(input("That's not it. Try again with another number."))
    print("You got it!")


