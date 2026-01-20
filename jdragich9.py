#JDragich Lab 9 
#Github test comment
name = input("Hello, what's your name?")

print("Menu")
print(">>>>>>>>>>>>>>>>>>>>>>>>>")
print("Option 1 - Joke")
print("Option 2 - Your Name 15x")
print("Option 3 - Inspiring Quote")
print("Option 4 - Guess My Number")
print("Option 5 - Convert Temperature")
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
elif (option == 4):
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
    def temp(f):
        c = (f - 32) * 5 / 9
        return c
f = int(input("What is today's temperature in Fahrenheit?"))
c = temp(f)
print("Wow, that's ", c, "in Celsius.")

