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






























