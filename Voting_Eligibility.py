age = int(input("Enter your age: "))

if age < 1 or age > 100:
    print("Invalid Age")
elif age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")