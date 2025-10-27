# class car:     # class car create ki gyi
#     def __init__(self,color,brand):    # constructor hai jo hamesha execute hota hai jb bhi nyi object banti hai
#         self.color = color    # CAR KI PROPERTIES HAIN
#         self.brand = brand
    
#     def drive(self):       # METHOD HAI JO CAR KO CHALATA HAI
#         print(f"{self.color} car chal rahi hai!")

# my_car = car("Blue", "BMW")             # ye teeno cheezien objects hain
# your_car = car("Red", "Audi")
# sarita_car = car("black","tata")

# my_car.drive()     # yha car kko chalaya ja rha hai 
# your_car.drive()

# practice 1
"""
Practice 1:
Ek class Banana — “Mobile”

Properties honi chahiye: color, brand

Method: call() – jab chalaye, print ho "{brand} mobile se call ho raha hai!"

Do object banao, run karo, test karo.
"""

class Mobile:
    def __init__(self,color, brand):
        self.color = color
        self.brand = brand

