import os


# return a list of strings with the names of the directories
def list_dir(dir_path):
    try:
        return [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]

    except FileNotFoundError:
        return []


# return a list of strings with the names of the files
def list_files(dir_path):
    try:
        return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

    except FileNotFoundError:
        return []


# where are we currantly?
current_dir = os.getcwd()

IS_RUNNING = True
while IS_RUNNING:   # allways run unless told otherwise
    # list the users different options
    print("\n1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit")

    # get the users choise
    choice = input("\n==> ")

    if choice == '1':
        directories = list_dir(current_dir)     # attempt to get directories
        if directories:                         # check for directories
            for directory in directories:
                print(directory)                # print out the directories
        else:
            print("No directories found.")

    elif choice == '2':
        new_dir_name = input("Name of directory to enter: ")    # get the new dir name

        # go back if the input '..' is detected
        if new_dir_name == '..':
            parent_dir = os.path.dirname(current_dir)
            if parent_dir != current_dir:
                current_dir = parent_dir
                print(f"Moved up to parent directory: {current_dir}")
            else:
                print("Already at the root directory.")

        # join path components (dir names or filenames) together, creates a valid & platform-independent path
        new_dir_path = os.path.join(current_dir, new_dir_name)

        # return true if the path exists and is a directory
        if os.path.exists(new_dir_path) and os.path.isdir(new_dir_path):
            current_dir = new_dir_path
            print(f"Entered directory: {current_dir}")
        else:
            print(f"Directory '{new_dir_name}' does not exist.")

    elif choice == '3':
        files = list_files(current_dir)     # attempt to get files
        if files:                           # check for files
            for file in files:
                print(file)                 # print out the filenames
        else:
            print("No files found in the current directory.")

    elif choice == '4':
        IS_RUNNING = False  # close the program

    else:
        print("Invalid choice. Please enter a valid option (1-4).")

print("Goodbye!")
