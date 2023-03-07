input_path = "A.txt"
output_path = "B.txt"

with open(input_path, "r") as input_file, open(output_path, "w") as output_file:
    output_file.write(input_file.read())

print(f"The contents of {input_path} have been copied to {output_path}.")
