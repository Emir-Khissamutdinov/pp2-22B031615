string = input("Enter a string: ")
upper_count = sum(1 for char in string if char.isupper())
lower_count = sum(1 for char in string if char.islower())

print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")
