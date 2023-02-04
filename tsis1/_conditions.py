# some things that could be mentioned here are given inside _booleans.py file

age = int(input("Enter your age: "))
if age < 18:
    print("You are not adult")
elif age == 18:
    print("You've just become adult")
else:
    print("You're undoubtedly an adult")

print()
if True: print("This is one-line if statement")

print()
print("Ternary") if True else print("Never printed") if 5 == 4 else print("Never-printed x2")
