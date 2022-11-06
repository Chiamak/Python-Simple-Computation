import math
# To calculate AREA of a CIRCLE
# pi(r^2)
def area_of_circle():
    pie = math.pi
    radius = int(input("r = "))
    print("pi = ", pie)
    area = pie * (radius ** 2)
    print("Area of a circle = pi(r^2)")
    print("The area is ", area)

area_of_circle()
