import os

path = "file.txt"

if os.path.exists(path) and os.access(path, os.R_OK):
    os.remove(path)
    print(f"The file {path} has been deleted.")
else:
    print(f"The file {path} does not exist or is not accessible.")
