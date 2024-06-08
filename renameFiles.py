import os
from tkinter import Tk, filedialog, messagebox
import re

def sanitize_filename(filename):
    # Removing any invalid characters from the filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def rename_al_files_in_folder(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".al"):
            file_path = os.path.join(folder_path, filename)
            rename_al_file(file_path)

def rename_al_file(file_path):
    # Read the first line of the file
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()

    if not first_line:
        print(f"The file {file_path} is empty or the first line is empty.")
        return

    # checking the first line to create a valid file name
    sanitized_name = sanitize_filename(first_line.replace(" ", ""))
    new_file_name = sanitized_name + ".al"
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

    # Check if the new file name already exists to avoid overwriting
    if os.path.exists(new_file_path):
        print(f"Cannot rename {file_path} to {new_file_name} because the file already exists.")
        return

    # Rename the file
    os.rename(file_path, new_file_path)
    print(f"File {file_path} has been renamed to: {new_file_name}")

def main():
    root = Tk()
    root.withdraw()
    user_choice = messagebox.askquestion("Select Option", "Do you want to select a file? (Select 'No' to choose a folder)")

    if user_choice == 'yes':
        file_path = filedialog.askopenfilename(title="Select an AL file", filetypes=[("AL files", "*.al")])
        if file_path:
            rename_al_file(file_path)
        else:
            print("No file selected.")
    else:
        folder_path = filedialog.askdirectory(title="Select a folder")
        if folder_path:
            rename_al_files_in_folder(folder_path)
        else:
            print("No folder selected.")

#Running the main function
if __name__ == "__main__":
    main()
