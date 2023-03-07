path = "file.txt"

with open(path, "r") as file:
    count = 0
    for line in file:
        count += 1

print(f"The file {path} contains {count} lines.")
