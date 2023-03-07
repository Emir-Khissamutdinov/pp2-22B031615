import os


def check_access(path):

    if not os.path.exists(path):
        print(f"{path} does not exist")
        return

    if not os.access(path, os.R_OK):
        print(f"{path} is not readable")
    else:
        print(f"{path} is readable")

    if not os.access(path, os.W_OK):
        print(f"{path} is not writable")
    else:
        print(f"{path} is writable")

    if not os.access(path, os.X_OK):
        print(f"{path} is not executable")
    else:
        print(f"{path} is executable")


path = "main.py"
check_access(path)
