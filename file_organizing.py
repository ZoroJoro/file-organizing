import os  # Module for interacting with the operating system
import shutil  # Module for high-level file operations
import tkinter as tk  # Module for creating graphical user interfaces
from tkinter import filedialog, messagebox  # Import specific tkinter dialogs and message boxes

def organize_files_by_extension(directory):
    # Check if the directory has already been organized
    organized = False
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            organized = True
            break

    if organized:
        messagebox.showinfo("Info", "This directory is already organized.")
        return

    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Get the file extension
        _, extension = os.path.splitext(file)
        extension = extension[1:]  # Remove the leading dot

        if not extension:  # Skip files without an extension
            continue

        # Create a subdirectory for the extension if it doesn't exist
        ext_dir = os.path.join(directory, extension)
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)

        # Check if a file named after the extension exists and use it for duplicates
        ext_file_path = os.path.join(directory, extension)
        if os.path.isfile(ext_file_path):
            dest_path = os.path.join(ext_dir, file)
        else:
            dest_path = os.path.join(ext_dir, file)

        # Move the file to the corresponding subdirectory
        src_path = os.path.join(directory, file)
        shutil.move(src_path, dest_path)

    messagebox.showinfo("Success", f"Files have been organized by extension in {directory}")

def choose_directory():
    directory = filedialog.askdirectory()  # Open a dialog to choose a directory
    if directory:  # If a directory is selected
        directory_var.set(directory)  # Set the selected directory to the StringVar

def apply_organization():
    directory = directory_var.get()  # Get the selected directory from the StringVar
    if directory:  # If a directory is selected
        organize_files_by_extension(directory)  # Organize files in the selected directory
    else:
        messagebox.showwarning("Warning", "Please choose a directory first.")  # Show a warning if no directory is selected

# Create the main window
root = tk.Tk()
root.title("File Organizer")  # Set the title of the window
root.geometry("256x128")  # Set the size of the window (width x height)

directory_var = tk.StringVar()  # Create a StringVar to hold the selected directory

# Create a button to choose the directory
choose_button = tk.Button(root, text="Choose Directory", command=choose_directory)
choose_button.pack(pady=10)  # Add the button to the window with padding

# Label to show the selected directory
directory_label = tk.Label(root, textvariable=directory_var)
directory_label.pack(pady=10)  # Add the label to the window with padding

# Create the Apply button
apply_button = tk.Button(root, text="Organize", command=apply_organization)
apply_button.pack(pady=10)  # Add the button to the window with padding

# Run the GUI event loop
root.mainloop()
