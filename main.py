#Shapes Class Hierarchy test program

from Circle import Circle
from Rectangle import Rectangle
from Square import Square

#Create a header for the polymorphism check
print("--- Polymorphism check ---")

#Create a list of shapes (the list is currently empty)
shapes = []

#Create two circles with different radii
c1 = Circle(0, 0, 4, "Circle_1")
c2 = Circle(0, 0, 9, "Circle_2")

#Create two rectangles with different dimensions
r1 = Rectangle(10, 20, "Rectangle_1")
r2 = Rectangle(16, 47, "Rectangle_2")

#Create a square
s1 = Square(10, "Square")

#Add all the shape objects to the list
shapes.append(c1)
shapes.append(c2)
shapes.append(r1)
shapes.append(r2)
shapes.append(s1)

#Loop through the list of shapes and print the name and area of each shape
for shape in shapes:
    print(f"{shape.name} Area = {shape.area}")

#Create a header for the getter/setter check
print("\n")
print("--- Getter/setter check ---")

#Test the Circle class
print(f"{c1.name} Current: {c1.radius} {c1.area}")
c1.radius = c1.radius * 2
print(f"{c1.name} Doubled: {c1.radius} {c1.area}")

#Test the Rectangle class
print("\n")
print(f"{r1.name} Current: {r1.length} {r1.width} {r1.area}")
r1.length = r1.length * 2
r1.width = r1.width * 2
print(f"{r1.name} Doubled: {r1.length} {r1.width} {r1.area}")

#Test the Square class
print("\n")
print(f"{s1.name} Current: {s1.side} {s1.area}")
s1.side = s1.side * 2
print(f"{s1.name} Doubled: {s1.side} {s1.area}")
