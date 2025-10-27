no_of_students = int(input("Enter total number of students in your class: "))
marks = []
for student in range(no_of_students):
    mark = int(input("Enter marks of students: "))
    marks.append(mark)
print(marks)


highest_mark = 0
for individual_mark in marks:
    if individual_mark > highest_mark:
        highest_mark = individual_mark
print(f"Highest mark of the class is : {highest_mark}")