import socket
import sys

ip = '127.0.0.1'
port = 50007

# Get message from command line argument or use "hello" by default
message = sys.argv[1] if len(sys.argv) > 1 else "hello"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, port))
    s.send(message.encode())  # Convert string to bytes
    data = s.recv(1024)

    print(data.decode('utf-8'))  # Decode byte data to string and print it
