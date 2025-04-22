# server.py

import socket

# Define host and port
HOST = '127.0.0.1'  # localhost
PORT = 65432  # Arbitrary non-privileged port

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print('Server is listening...')
    # Accept incoming connection
    conn, addr = s.accept()
    print('Connected by', addr)
    
    # Communication loop
    while True:
        # Receive data from the client
        data = conn.recv(1024).decode()
        if not data:
            break
        print('Client:', data)
        # Send data to the client
        message = input('Server: ')
        conn.sendall(message.encode())
