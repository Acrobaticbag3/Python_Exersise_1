import os
# might have accidentaly made this one wrong... as in too good?


# recursively print directory structure starting from dir_path.
def print_sub(dir_path):
    if os.path.isdir(dir_path):
        print(os.path.basename(dir_path))
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)
            if os.path.isdir(item_path):
                print_sub(item_path)


# Start of Main
dir_path = os.getcwd()
print_sub(dir_path)
