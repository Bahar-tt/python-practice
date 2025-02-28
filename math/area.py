#تمرین مساحت مستطیل

def rectangle_area(length,width):
    return length * width
    

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))
area = rectangle_area (length , width)
print(f"The area of the rectangle is:{area}")

#تمرین مساحت دایره
import math
def circle_area(radius):
    return math.pi * (radius**2)
    #return 3.14 * (radius**2)


radius = float(input("Enter the radius of the circle:"))
area = circle_area (radius)
print(f"The area of the circle:{area}")