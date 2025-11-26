import socket

def get_system_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

get_system_info()