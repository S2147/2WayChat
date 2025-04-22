# client.py

import socket

# Define host and port
HOST = '127.0.0.1'  # localhost
PORT = 65432  # Arbitrary non-privileged port

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to server
    s.connect((HOST, PORT))
    
    # Communication loop
    while True:
        # Send data to the server
        message = input('Client: ')
        s.sendall(message.encode())
        # Receive data from the server
        data = s.recv(1024).decode()
        print('Server:', data)
