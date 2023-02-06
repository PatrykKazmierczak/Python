# if / else conditional statement
import condition as condition

if condition:
    do this
else:
    do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))

if height >= 120:
    print("You are taller than 120 feet.")
else:
    print("You are not taller than 120 feet.")

# program to check if given number is odd or even

number = int(input("Which number do you want to choose"))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))

if height >= 120:
    print("You are taller than 120 feet.")
    age = int(input("How old are you? "))
    if age <= 18:
        print("Please pay 7 $.")
    else:
        print("Please pay 12$ ")
else:
    print("You are not taller than 120 feet.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))

if height >= 120:
    print("You can ride rollercoaster.")
    age = int(input("How old are you? "))
    if age < 12:
        print("Please pay 7 $.")
    elif age <= 18:
        print("Please pay 12$ ")
    elif age <= 22:
        print("Please pay 15$ ")
    else:
        print("Please pay 18$ ")
else:
    print("You have to grow taller before you can ride.")


























