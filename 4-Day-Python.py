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

