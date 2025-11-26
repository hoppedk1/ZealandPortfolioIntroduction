import shutil
import string
import os

for drive in string.ascii_uppercase:
    drive_path = f"{drive}:/"
    if os.path.exists(drive_path):
        total, used, free = shutil.disk_usage(drive_path)
        percent_free = (free / total) * 100
        print(f"Drive {drive}:")
        print(f"  Total: {total // (2**30)} GiB")
        print(f"  Used: {used // (2**30)} GiB")
        print(f"  Free: {free // (2**30)} GiB ({percent_free:.2f}%)")
        if percent_free < 20:
            print("  WARNING: Less than 20% disk space remaining!")