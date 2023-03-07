import os

path = "lab6/dir-and-files_3.py"

if os.path.exists(path):
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print("Path exists!")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print("Path does not exist.")
