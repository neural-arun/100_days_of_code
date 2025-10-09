heights = []
no_of_students = int(input("Enter Total number of student: "))
for student in range(0,no_of_students):
    student_height = int(input("Enter student height: "))
    heights.append(student_height)
print(heights)

all_heights= 0
for height in heights:
    all_heights += height
print(f"Sum of all heights of all students is {all_heights}")

avg = all_heights / no_of_students
print(f"Average of heights of all students is: {avg}")