import socket
# tager meget lang tid, så jeg scanner kun 1-100
def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_ip = "8.8.8.8"  # Google's public DNS server
    ports_to_scan = range(1, 101)  # Common ports 1-1024
    open_ports = scan_ports(target_ip, ports_to_scan)
    print(f"Open ports on {target_ip}: {open_ports}")