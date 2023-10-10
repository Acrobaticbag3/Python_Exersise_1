import os


# Returns the number of directories
def count_directories(dir_path):
    return len([d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))])   # list comprehension iterates over each entry in the directory


# Returns the number of files
def count_files(dir_path):
    return len([f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))])  # list comprehension iterates over each entry in the directory


# start of main
current_dir = os.getcwd()
print("Current Absolute Path:", current_dir)

# call & stor value from "count_directories"
num_directories = count_directories(current_dir)

# call & stor value from "count_files"
num_files = count_files(current_dir)

# print our stuff
print(f"Below me I have {num_directories} directories/folders")
print(f"This directory contains {num_files} file(s)")
