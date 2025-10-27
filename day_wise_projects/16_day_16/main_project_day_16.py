"""
My Daily Challenge: Define a MedicalTest Class
Objective: Create a blueprint for a medical test, then create several instances (objects) of
it.
Steps:
1. Create a class named MedicalTest.
2. Define the constructor (__init__) method. It should take name, patient_name, and
normal_range (a tuple like (90, 120)) as parameters.
3. Inside the constructor, create attributes for these parameters. Also, create an
attribute called result_value and initialize it to None.
4. Create a method called record_result(self, value). This method should set
the self.result_value attribute to the value that is passed in.
5. Create another method called get_interpretation(self). This method should:
First, check if self.result_value is still None. If it is, return "Result not
yet recorded."
Use if/elif/else to compare self.result_value against the
self.normal_range.
return a string: "LOW", "NORMAL", or "HIGH".
6. Outside the class:
Create an object for a blood sugar test: sugar_test =
MedicalTest(name="Blood Sugar", patient_name="Jane Doe",
normal_range=(70, 100)).
Create an object for a cholesterol test: cholesterol_test =
MedicalTest(name="Cholesterol", patient_name="Jane Doe",
normal_range=(100, 200)).
Record a result for the sugar test: sugar_test.record_result(85).
Print the interpretation for the sugar test:
print(sugar_test.get_interpretation()).
Print the interpretation for the cholesterol test (before recording a result) to
see the default message
"""


class MedicalTest:
    """
    2. Define the constructor (__init__) method. It should take name, patient_name, and
     normal_range (a tuple like (90, 120)) as parameters.
    """
    def __init__(self,name,patient_name,normal_range):
        self.name = name
        self.patient_name = patient_name
        self.normal_range = normal_range
        result_value = None
    def record_result(self, value):
        self.result_value = value

