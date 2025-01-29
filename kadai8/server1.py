import socket
import sys

ip = '127.0.0.1'
port = 50007

message_counter = 1  # Initialize message counter

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))

    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')  # Convert byte data to string
                print(f"Message {message_counter}: {message}, from {addr}")
                if message.lower() == "stop":
                    print("Stopping server...")
                    sys.exit()  # Stop the server
                message_counter += 1
                conn.send(b"Received: " + data)
