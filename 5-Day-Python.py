# # Loops
# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
#     print(fruits)
#     print(len(fruits))
#     print(fruits[0])
#     print(fruits[-1])
#     print(fruits[1:3])
#     print(fruits[::2])
#     print(fruits[::-1])
#
# funny_text = ["Nobody is interested in my underpants\n"]
#
# for underpants in funny_text:
#     print(underpants * 20)
#
# student_heights = input("Enter students heights: ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # print(student_heights)
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# # print(total_height)
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# # print(number_of_students)
#
# number_of_students = len(student_heights)
# average_heights = round(total_height / number_of_students)
# print(average_heights)

# student_scores = input("Input a list of student").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(max(student_scores))
# print(min(student_scores))
#
# table = [125, 145, 25, 465]
# print(max(table))

student_scores = [25, 256, 54, 87, 80, 555]

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

student_scores_1 = [25, 256, 54, 87, 80, 555]

student_scores_2 = [2, 126, 4, 569, 81, 52]

for x in student_scores_1:
    for y in student_scores_2:
        print(x, y)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

table = [1, 2, 3, 4, 5]

for number in range(1, len(table)):
    print(number)

for number in range(0, 5):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

# 1 + 2 + 3 = 6

total = 0
for number in range(1, 4):
    total += number
print(total)

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45

total = 0
for number in range(1, 10):
    total += number
print(total)

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

total = 0
for number in range(1, 11):
    total+= number
print(total)

# print 1 4 7 10

total = 0
for number in range(1, 11, 3):
    print(number)

# calculate even numbers

total = 0
for number in range(2, 101, 2):
    total += number
print(total)


total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)

# calculate odd numbers

total2 = 0
for number in range(1, 101):
    if number % 2 != 0:
        total2 += number
print(total2)



# Program FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz {number}")
    elif number % 3 == 0:
        print(f"Fizz {number}")
    elif number % 5 == 0:
        print(f"Buzz {number}")
    else:
        print(f"{number}")




import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"Himport random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")ow many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")


































