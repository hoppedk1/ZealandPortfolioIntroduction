import psutil

for proc in psutil.process_iter(['pid', 'name']):
    try:
        print(f"Process: {proc.info['name']}, PID: {proc.info['pid']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass