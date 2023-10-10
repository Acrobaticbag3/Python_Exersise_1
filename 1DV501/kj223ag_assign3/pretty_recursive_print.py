import os
# might have accidentaly made this one wrong... as in too good?


# recursively print directory structure starting from dir_path.
def print_sub(dir_path, indent=''):
    if os.path.isdir(dir_path):
        print(indent + os.path.basename(dir_path))
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)
            if os.path.isdir(item_path):
                # increase indentation for subdirectories
                print_sub(item_path, indent + "  ")


# Start of Main
dir_path = os.getcwd()
print_sub(dir_path)
