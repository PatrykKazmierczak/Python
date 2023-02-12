# import random
# #import my_module
#
# random_integer = random.randint(100, 200)
# print(random_integer)
#
# #print(my_module)
#
# random_float = random.random() * 5
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")
#
# # Simple Heads and Tails program
#
# random_number = random.randint(0, 1)
# if random_number == 1:
#     print("Heads")
# else:
#     print("Tails")
# print(random_number)

# List

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

states_of_america.insert(3,"test")
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