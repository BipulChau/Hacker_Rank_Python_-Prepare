# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second-lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second-lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second-lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


# new_students = list(map(lambda e: {e[0]: e[1]}, students))
# print(new_students)
#
# marks = []
#
# for e in new_students:
#     for v in e.values():
#         marks.append(v)
#
# print(marks)
# marks = sorted(marks, reverse=True)
# print(marks)

def get_marks(student):
    return student[1]


students.sort(key=lambda i: i[1], reverse=True)  # sort the entire students list in descending order of marks
print(students)

students_list_excluding_lowest_grade = list(filter(lambda j: j[1] != students[-1][1], students))  # filter the elements which have the lowest marks
print(students_list_excluding_lowest_grade)

# students_list_with_second_lowest_grade = list(filter(lambda k: k[1] == students_list_excluding_lowest_grade[-1][1], students_list_excluding_lowest_grade))  # filter the elements whose marks are not equal to second-lowest marks
students_list_with_second_lowest_grade = filter(lambda k: k[1] == students_list_excluding_lowest_grade[-1][1], students_list_excluding_lowest_grade)  # filter the elements whose marks are not equal to second-lowest marks

print(students_list_with_second_lowest_grade)

for e in students_list_with_second_lowest_grade:
    print(e[0])

