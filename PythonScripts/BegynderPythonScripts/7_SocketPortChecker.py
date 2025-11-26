import socket

def check_port(host, port, timeout=3):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return True
        except (socket.timeout, socket.error):
            return False

host = 'google.com'
port = 443
if check_port(host, port):
    print(f"Port {port} on {host} is open.")
else:
    print(f"Port {port} on {host} is closed.")