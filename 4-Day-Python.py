import random
#import my_module

random_integer = random.randint(100, 200)
print(random_integer)

#print(my_module)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Simple Heads and Tails program

random_number = random.randint(0, 1)
if random_number == 1:
    print("Heads")
else:
    print("Tails")
print(random_number)

List

states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia"]
print(states_of_america[0])
print(states_of_america[-1])

states_of_america[1] = "Pen"

states_of_america.append("New States")

print(states_of_america)

states_of_america.extend(["New state 1", "New state 2"])

print(states_of_america)

# list.append(x)
# list.insert(i, x)
# list.extend(iterable)
# list.remove(x)
# list.pop([i])
# list.clear()
# list.index(x[, start[, end]])
# list.count(x)
# list.sort(*, key=None, reverse=False)
# list.reverse()
# list.copy()

states_of_america.insert(3, "test")
print(states_of_america)
states_of_america.remove("Colorado")
print(states_of_america)
# states_of_america.clear()
# print(states_of_america)
states_of_america.index("Delaware", 0, 9)
print(states_of_america)
states_of_america.reverse()
print(states_of_america)
states_of_america.copy()
print(states_of_america)



import random

names_string = input("Give me everybody's names, separated by a comma")
names = names_string.split(", ")
numer_of_items = (len(names))

random_choice = random.randint(0, numer_of_items-1)
person = names[random_choice]
print(person)
print(person)



import random
#import my_module

random_integer = random.randint(100, 200)
print(random_integer)

#print(my_module)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Simple Heads and Tails program

random_number = random.randint(0, 1)
if random_number == 1:
    print("Heads")
else:
    print("Tails")
print(random_number)

List

list.append(x)
list.insert(i, x)
list.extend(iterable)
list.remove(x)
list.pop([i])
list.clear()
list.index(x[, start[, end]])
list.count(x)
list.sort(*, key=None, reverse=False)
list.reverse()
list.copy()

states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia"]
print(states_of_america[0])
print(states_of_america[-1])

states_of_america[1] = "Pen"

states_of_america.append("New States")

print(states_of_america)

states_of_america.extend(["New state 1", "New state 2"])

print(states_of_america)

# list.append(x)
# list.insert(i, x)
# list.extend(iterable)
# list.remove(x)
# list.pop([i])
# list.clear()
# list.index(x[, start[, end]])
# list.count(x)
# list.sort(*, key=None, reverse=False)
# list.reverse()
# list.copy()

states_of_america.insert(3, "test")
print(states_of_america)
states_of_america.remove("Colorado")
print(states_of_america)
# states_of_america.clear()
# print(states_of_america)
states_of_america.index("Delaware", 0, 9)
print(states_of_america)
states_of_america.reverse()
print(states_of_america)
states_of_america.copy()
print(states_of_america)



import random

names_string = input("Give me everybody's names, separated by a comma")
names = names_string.split(", ")
numer_of_items = (len(names))

random_choice = random.randint(0, numer_of_items-1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay)

person_who_will_pay = random.choice(names)
print(person_who_will_pay)

print(len(states_of_america))

nested list
dirty_dozen = ["Strawberry", "Spinach", "Grapes"]

fruits = ["Strawberry", "Nectarines", "Apples"]
vegetables = ["Spinach", "Tomatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)


row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]

position = input("Where do you want to put treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")


row1 = [" ", " ", " ", " ", " "]
row2 = [" ", " ", " ", " ", " "]
row3 = [" ", " ", " ", " ", " "]
row4 = [" ", " ", " ", " ", " "]
row5 = [" ", " ", " ", " ", " "]
row6 = [" ", " ", " ", " ", " "]
row7 = [" ", " ", " ", " ", " "]
row8 = [" ", " ", " ", " ", " "]

map = [row1, row2, row3, row4, row5, row6, row7, row8]

position = input("Where do you want to put treasure ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical -1][horizontal -1] = "x"

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n")


base_hours = 10000

days_year = 365

days_hours = 24

year_hours = days_year * days_hours

base_years = base_hours / year_hours

print(base_years)

import random

man_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

if man_choice == 0:
    print("Rock")
elif man_choice == 1:
    print("Paper")
elif man_choice == 2:
    print("Scissors")

man_score = int(man_choice)


computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print("Rock")
elif computer_choice == 1:
    print("Paper")
elif computer_choice == 2:
    print("Scissors")

computer_score = int(computer_choice)


if man_choice == 1 and computer_choice == 1:
    print("draw")
elif man_choice == 0 and computer_choice == 0:
    print("draw")
elif man_choice == 2 and computer_choice == 2:
    print("draw")
elif man_choice == 1 and computer_choice == 0:
    print("Man won")
elif computer_choice == 0 and man_choice == 1:
    print("Computer won")
elif man_choice == 2 and computer_choice == 1:
    print("Man won")
elif computer_choice == 1 and man_choice == 2:
    print("Computer won")

import random
user_choice = int(input("What do you choose? Type 0 Rock, 1 Paper, 2 Scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"Computer choice {computer_choice}")

if user_choice == 0 and computer_choice ==2:
    print("You win")
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice == user_choice:
    print("It's a draw")
elif user_choice > computer_choice:
    print ("You win")
elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number")














