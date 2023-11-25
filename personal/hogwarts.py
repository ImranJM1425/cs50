# # Lists, length
# # 1)
# students = ["Hermione", "Herry", "Ron"]

# print (students[0])
# print (students[1])
# print (students[2])

# # 2) Using for loop in lists
# students = ["Hermione", "Herry", "Ron"]

# for student in students:
#     print(student)

# # 3) Using range and len
# students = ["Hermione", "Harry", "Ron"]

# for i in range (len(students)):
#     print (i+1, students[i])

# # 4) Using dicts. "Key":"Value"
# students = {
#     "Hermione": "Gryffindor", 
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin",
#     }

# for student in students:
#     print(student, students[student], sep=", ")

# 5) Using dicts in lists
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")