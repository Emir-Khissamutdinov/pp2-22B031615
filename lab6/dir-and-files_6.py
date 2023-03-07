for letter_code in range(ord("A"), ord("Z") + 1):
    letter = chr(letter_code)
    filename = f"{letter}.txt"
    with open(filename, "w") as file:
        file.write("")
    print(f"Created file {filename}.")
