import hashlib
import os

def get_file_hash(filename, hash_algo='sha256'):
    hash_func = hashlib.new(hash_algo)
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def save_hash(filename, hashfile, hash_algo='sha256'):
    file_hash = get_file_hash(filename, hash_algo)
    with open(hashfile, 'w') as f:
        f.write(file_hash)
    print(f"Hash saved to {hashfile}")

def check_hash(filename, hashfile, hash_algo='sha256'):
    if not os.path.exists(hashfile):
        print("Hash file does not exist.")
        return
    current_hash = get_file_hash(filename, hash_algo)
    with open(hashfile, 'r') as f:
        saved_hash = f.read().strip()
    if current_hash == saved_hash:
        print("File has not changed.")
    else:
        print("File has changed!")

# Example usage:
#save_hash('meetingSchedule.txt', 'example.txt.hash') # skal nok gemmes et seperat sted i virkeligheden
check_hash('meetingSchedule.txt', 'example.txt.hash') # ditto