
#JDragich Lab 10 Final Project 
name = input("Hello, what's your name?")

print("Menu")
print(">>>>>>>>>>>>>>>>>>>>>>>>>")
print("Option 1 - Joke")
print("Option 2 - Your Name 15x")
print("Option 3 - Inspiring Quote")
print("Option 4 - Guess My Number")
print("Option 5 - Convert Temperature")
print("Option 6 - Escape the Staff Meeting Game")
print("<<<<<<<<<<<<<<<<<<<<<<<<<")
print("Hello,", name, ". Please enter an option.")
option = int(input())
if (option == 1):
    print("I stayed up all night trying to figure out where the sun went.")
    print("Then, it dawned on me.")
if (option == 2):
    for i in range(15):
        print(name)
if (option == 3):
    rep = int(input("Type a number 1-10."))
    for i in range(rep):
        print("We can rebuild him. We have the technology.")
if (option == 4):
    x = int(input("What's your guess?"))
    while (x != 42):
        while x <0 or x >100:
            x = int(input("Please try again with a number 1-100. What's your guess?"))
        if (x < 42):
                print("That's too low. Try again. What's your guess?")
        elif (x > 42):
                print ("That's too high! Try again. What's your guess?")
        x = int(input("What's your guess?"))
    print ("Yes, you got it!")
if (option == 5):
    f = int(input("What is today's temp in F?"))
    def temp(f):
        c = (f - 32) * 5 / 9
        return c
    c = temp(f)
    print("Wow, that's ", c, "in Celsius.")
elif (option == 6):
    print("You are now a high school teacher.")
    subject = input("What subject would you like to teach?")
    print("It's a Friday in March.")
    print("You are very tired.")
    print("Your goal is to get out of the", subject, "building and to your car without being pulled into a staff or parent meeting.")
    print("Let's do this.")
    choice = int(input("Type 1 if you want to leave your classroom and take the stairs. Type 2 if you'd like to take the elevator. Type 3 if you'd like to go out through the window."))
    while (choice > 3):
         choice = int(input("That's too high. Please enter a choice between 1 and 3."))
    def springbreak():
        print("Don't worry. Spring Break is almost here.")
    if choice == 3:
        print("Your classroom was on the second floor. Why would you go out the window? The principal called 911. You still have to go to the makeup meeting. Game over.")
        springbreak()
    if choice == 2:
        print("The elevators doors open with a loud ding. Did the principal hear you?")
        import random
        roll = random.randint(1, 6)
        if (roll < 5):
            print("You rolled a ", roll, ". Your principal waves and offers to walk you to the staff meeting. Game over.")
        else:
            print("You rolled a ", roll, ". The hallway is clear. Run for the door!")
        springbreak()
    if choice == 1:
        print("Rats! There's a student and an angry-looking parent. Can you turn around? Did they see you?")
        import random
        roll2 = random.randint(1, 6)
        if (roll2 < 5):
            print("You rolled a ", roll2,". Nope! They saw you. You spend the next hour in an exhausting meeting.")
        else:
            print("You rolled a ", roll2,". You sneak back and take the back stairs down to the parking lot. Don't look back!")
        springbreak()



