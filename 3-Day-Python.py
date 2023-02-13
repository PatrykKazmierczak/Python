# if / else conditional statement
# import condition as condition
#
# if condition:
#     do this
# else:
#     do this

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

# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

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

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(round(bmi_as_int, 2))

if bmi_as_int < 18.5:
    print(f"Your bmi is {bmi_as_int}, You are underweight.")
elif bmi_as_int >= 18.5 and bmi_as_int < 25:
    print(f"Your bmi is {bmi_as_int}, You are normal.")
elif bmi_as_int >= 25 and bmi_as_int < 30:
    print(f"Your bmi is {bmi_as_int}, You are overweight.")
elif bmi_as_int >= 30 and bmi_as_int < 35:
    print(f"Your bmi is {bmi_as_int}, You are obese.")
else:
    print(f"Your bmi is {bmi_as_int}, You are clinically obese.")

year = int(input("What year you want to check" ))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("You can ride rollercoaster.")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5 $.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are 7 $ ")
    elif age >= 45 and age <= 65:
        print("Tickets are for free")
    else:
        bill = 18
        print("Adult tickets are 18$ ")
    wants_foto = input("Do you want to photo taken? Y or N.")
    if wants_foto == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("You have to grow taller before you can ride.")

print("Welcome to Phyton Pizza Deliveries")
size = input("What size pizza do you want? S, M, L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
bill =0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is{bill}")
if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is{bill}")
if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is{bill}")


print("Welcome to Phyton Pizza Deliveries")
size = input("What size pizza do you want? S, M, L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    if size == "S":
        bill += 1

print(f"Your final bill is{bill}")

print("Welcome to the Love Calculator")
name1 = input("What is your name?\n ")
name2 = input("What is your name?\n ")

combined_name = name1 + name2
lower_case_string = combined_name.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}")

print('''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
 choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across').lower()
 if choice2 == "wait":
     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
     if choice3 == "red":
         print("Game over")
     elif choice3 == "yellow":
         print("You win")
     elif choice3 == "blue":
         print("Game over")
     else:
         print("You choose a door that doesn't exist. Game over.")
 else:
     print("You got attacked by angry trout")
else:
    print("You fell into a hole. Game over.")

    # Create own ASCII game

print("Welcome to Quiz Game")
print("Your mission is to correct answer for question")

choose1 = input('Which type of transport is slower "bike" or "motorbike"')
    if choose1 == "bike":
        print("You won the game")
        print(''' 
                   _     _                 _      
| |   (_)               | |     
| |__  _  ___ _   _  ___| | ___ 
| '_ \| |/ __| | | |/ __| |/ _ \
| |_) | | (__| |_| | (__| |  __/
|_.__/|_|\___|\__, |\___|_|\___|
               __/ |            
              |___/    
 ''')
    else:
        print('''   _____
           /     \/_
          //\__(\_\
          |\ ^  ^ |
         .//_O \O_ \
          \_  (_)  /
           \  \_/ /
         __/\    /\__
        /  \ \  / /  \
       /    \/\/\/    \
      /   |    .   |   \
     /    |    .   |    \ ''')
        print("You lost a game funny boy")


print("Welcome to Treasure Island. Your mission is to find the treasure")























