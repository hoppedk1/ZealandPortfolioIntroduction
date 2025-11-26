import os
import stat

def has_world_read_write(filepath):
    mode = os.stat(filepath).st_mode
    return (mode & stat.S_IROTH) and (mode & stat.S_IWOTH)

def find_world_rw_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                if has_world_read_write(filepath):
                    print(filepath)
            except Exception as e:
                # Skip files we can't stat
                continue

if __name__ == "__main__":
    search_dir = "."  # Change to your target directory
    find_world_rw_files(search_dir)