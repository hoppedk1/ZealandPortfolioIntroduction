import os

file_path = input("Enter the path to the file you want to check: ")

if os.path.isfile(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")