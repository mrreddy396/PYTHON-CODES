class Student:
    def __init__(self,name,rollNumber):
        self.name=name
        self.rollNumber=rollNumber
    def display(self):
        print("Name :",self.name)
        print("RollNumber :",self.rollNumber)
student1=Student("Alice",29)
student1.display()