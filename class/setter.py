class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            print("Radius is Positive!!")
        else:
            self.__radius = value

    @property
    def area(self):
        return 3.14 * self.__radius ** 2
    

c = Circle(5)
print(f"Area: {c.area}")

c.radius = 8
print(f"Area after update: {c.area}")
        