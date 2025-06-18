#logical operators = or and not
"""
temp = -1
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else: 
    print("The outdoor even is still scheduled.")
"""

""""""
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

