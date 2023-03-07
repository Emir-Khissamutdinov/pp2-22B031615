import os


def list_directories(path):
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            print(name)


def list_files(path):
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            print(name)


def list_all(path):
    for name in os.listdir(path):
        print(name)


path = "/path/to/directory"
print("Directories only:")
list_directories(path)
print("\nFiles only:")
list_files(path)
print("\nAll directories and files:")
list_all(path)
