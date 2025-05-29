import socket

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout 
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open on {host}")
    else:
        print(f"Port {port} is closed on {host}")
    sock.close()

def scan_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

if __name__ == "__main__":
    host = '127.0.0.1'  # Replace with the target IP address or hostname
    start_port = 1  # Replace with the starting port number
    end_port = 1024  # Replace with the ending port number

    scan_ports(host, start_port, end_port)
