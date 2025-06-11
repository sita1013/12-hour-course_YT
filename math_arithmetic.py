"""
friends = 0 

friends += 1 #augmented assignment operators +=
friends -= 2
friends *= 3
friends /= 3
friends **= 2
friends %= -1 #modulous
print(friends)"""

""""
x = 3.14
y = 4
z = 5

result = round(x)
result = abs(y)
result = pow(4, 3)
result = max(x, y, z)
result = min(x, y, z)
print(result)
"""

"""
import math

x = 9.9
print(math.pi)
print(math.e)
#result = math.sqrt(x)
result = math.ceil(x) # always round a number up
result = math.floor(x) #always round a number down
print(result)
"""
#############################################################
"""
#exercise 1 : circle circum
import math

radius = float(input("Enter the radius: "))
circumference = math.pi * 2 * radius

print(f"The circumference is {round(circumference, 2)}cm.")
"""

"""
#exercise 2 : area of a circle
import math 

radius = float(input("Enter the radius: "))
area = math.pi * radius**2
print(f"The area of the circle is {round(area, 2)}cm².")"""

#exercise 3 : hypotenus of right angle triagle
import math

a = float(input("Enter side 'a' of the triangle: "))
b = float(input("Enter side 'b' of the triangle: "))

c = math.sqrt(a**2 + b**2)

print(f"The hypotenus of the triangle is {round(c, 2)}")