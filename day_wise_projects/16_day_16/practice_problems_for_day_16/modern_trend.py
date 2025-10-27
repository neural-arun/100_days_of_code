from dataclasses import dataclass
@dataclass
class Student:
    name: str
    roll: int
    marks: float
# Auto __init__, __repr__ generated!

s1 = Student("Arun",34,98)
print(s1)