#logfile_path = "/var/log/auth.log"
logfile_path = "auth.log" # til testing i Windows
try:
    with open(logfile_path, "r") as logfile:
        for line in logfile:
            if "failed" in line.lower():
                print(line, end="")
except FileNotFoundError:
    print(f"Logfile not found: {logfile_path}")
except Exception as e:
    print(f"An error occurred: {e}")