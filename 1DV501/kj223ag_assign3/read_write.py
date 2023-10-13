# Not done, does not work
import os


# Read text file and return a list of strings containing each line in the file.
def read_file(file_path):
    try:
        with open(file_path) as f:
            for i in file_path:
                lst = f.read()
                print(lst)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


# Write content of the list lines to the a file specified by file_path.
def write_file(lines, file_path):
    print()


# Program starts
path = os.getcwd()

# Read text file
# lst = read_file(path)
# print(f"Read {len(lst)} lines from file {path}")

# Write text file
path = os.getcwd() + "/mamma_mia.txt"
print(read_file(path))
# write_file(lst, path)
print("Text saved in file", path)
