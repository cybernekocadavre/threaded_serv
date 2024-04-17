#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# serv.py

import socket
import threading
import sys

# Dictionary to store connected clients and their usernames
clients = {}

# List to store message history
message_history = []

# Echo server function
def echo_server(client_socket, client_address, username):
    print(f"Connected to {client_address} as {username}")
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        message = f"{username}: {data.decode()}"
        print(f"Received from {client_address}: {message}")
        
        # Add message to history
        message_history.append(message)
        
        # Send the message to all clients
        for client in clients.values():
            client.sendall(message.encode())
            
    print(f"Disconnected from {client_address} as {username}")
    client_socket.close()
    del clients[username]

# Function to handle incoming client connections
def handle_client_connections(server_socket):
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        
        # Prompt for username and receive from client
        client_socket.sendall("Enter your username: ".encode())
        username = client_socket.recv(1024).strip().decode()
        
        # Add client to dictionary
        clients[username] = client_socket
        
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=echo_server, args=(client_socket, client_address, username))
        client_thread.start()

# Main function
def main():
    # Set up server socket
    server_host = '127.0.0.1'
    server_port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print(f"Server listening on {server_host}:{server_port}")

    # Start a thread to handle incoming client connections
    client_handler_thread = threading.Thread(target=handle_client_connections, args=(server_socket,))
    client_handler_thread.start()

if __name__ == "__main__":
    main()






