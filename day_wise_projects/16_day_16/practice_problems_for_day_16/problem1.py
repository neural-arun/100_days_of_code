"""
Create a  Student  class with:
 Attributes:  name ,  roll_number ,  marks 
Method:  display_info()  jo student ki details print kare
 Expected Output:
 Name: Rahul Sharma
 Roll: 101
 Marks: 85
 """

class Student:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll_number}")
        print(f"Marks: {self.marks}")

student1 = Student("Arun",16,96)
student1.display_info()