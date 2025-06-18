#logical operators = or and not
"""
temp = -1
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else: 
    print("The outdoor even is still scheduled.")
"""

"""
temp = 0
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside.")
    print("It is sunny.")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside.")
    print("It is cloudy.")
else:
    print("Something else.")
"""
#conditional expression
"""
num = -5
print("Positive" if num > 0 else "Negative")


num = 6
result = "Even" if num % 2 == 0 else "Odd"
print(result)
"""

user_role = "guest"

access_level = "Full Access" if user_role == "admin" else "Limited Acess"
print(access_level)
