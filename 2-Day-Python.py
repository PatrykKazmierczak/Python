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
