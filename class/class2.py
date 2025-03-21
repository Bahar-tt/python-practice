class person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def introduce(self):
        print(f"Hello! I am {self.name}, {self.age} years old from {self.city}")
    def is_adult(self):
        return self.age > 18
    def move_city(self, new_city):
        self.city = new_city
        print(f"{self.name} moved to {self.city}")

p1 = person("Bahar", 36, "Damghan")
p2 = person("Sara", 8, "Lahijan")
p1.introduce()
print(p1.is_adult())
p2.introduce()
print(p2.is_adult())
p1.move_city("Esfahan")
p1.introduce()