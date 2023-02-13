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

student_heights = input("Enter students heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights)
