print("Hello, World!")

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percentage = tip / 100
total_tip = bill * tip_as_percentage
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 3)

print(final_amount)

# exercises

print("Welcome to the clip calculator.")
bill = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

tip_as_percentage = tip / 100
total_tip = tip_as_percentage * bill
total_bill = bill + total_tip
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(len("Hello"))

# print first letter
print("Hello"[0])
# print last letter
print("Hello"[4])


print (4565 + 547483)

# Phyton Data Types
# Integer 98787
# Float 3.13432
#Boolean True False

name_char = len(input("What is your name"))
new_name_char = str(name_char)
print("Your name has " + new_name_char + " characters.")

# check type of input
print(type(name_char))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

a = int(123)
print(type(a))

print(70 + float("100.5"))

print(str(70) + str(100))


# Example of solution -> number 59  = 5 + 9 = 12

a = int(input("Please write number from 10 - 99"))
b = str(a)
c = str(a)

d = b[0]
e = c[1]

f = int(d)
g = int(e)

print(f + g)

3 + 5
7 - 4
3 * 2
6 / 3
2 ** 2  #power

Pemdas
()
**
*
/
+ -

print(3 * 3 + 3 / 3 - 3)

height = input("enter your height in m: ")
weight = input("enter your weight in kg ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print (round(bmi_as_int, 3))


























