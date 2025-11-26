import os

directory = input("Enter the directory path: ") # svar fx "5_convertfiles" for mappen

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        old_path = os.path.join(directory, filename)
        new_filename = filename[:-4] + ".md"
        new_path = os.path.join(directory, new_filename)
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")