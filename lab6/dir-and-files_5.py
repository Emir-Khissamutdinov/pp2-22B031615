my_list = ["apple", "banana", "orange", "pear"]

path = "file.txt"

with open(path, "w") as file:
    for item in my_list:
        file.write(f"{item}\n")

print(f"The list has been written to {path}.")
