class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

students = [Student(f"Student_{i}", i, 75) for i in range(100)]

for s in students:
    print(f"{s.name} - Roll: {s.roll}, Marks: {s.marks}")
