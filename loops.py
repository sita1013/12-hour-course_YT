"""
name = input("Enter your name: ")
while name == " ":
    print("You did not enter your name.")
    name = input("Enter your name: ")
print(f"Hello {name}.")

age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be negative.")
    age = int(input("Enter your age: "))
print(f"Your are {age} years old.")

food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}.")
    food = input("Enter another food you like (q to quit): ")
print("bye bye")"""

"""
for i in range(1, 11):
    print(i)

for i in reversed(range(1, 11)):
    print(i)
print("Happy New Year!")

for i in range(1, 11, 3):
    print(i)

credit_card = "1234-5678-9101"
for i in credit_card: 
    print(i)
"""
for i in range(1, 21):
    if i == 13:
        continue
    elif i == 19:
        break
    else: 
        print(i)


