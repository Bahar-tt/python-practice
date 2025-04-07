class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def introduce(self):
         print(f"My name is {self.name} and I am {self.age} years old.")
    
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old, studying {self.major}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"Hello, my name is {self.name}. I teach {self.subject}.")


s1 = Student("Sara", 22, "Computer science")
t1 = Teacher("Ali", 40, "Math")
s1.introduce()
t1.introduce()

