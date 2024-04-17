#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import socket
import threading

# Dictionary to store user names and their corresponding sockets
users = {}

# List to store message history
message_history = []

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    
    # Prompt user for username
    client_socket.sendall(b"Enter your username: ")
    username = client_socket.recv(1024).decode().strip()
    
    # Add user to dictionary
    users[client_socket] = username
    
    try:
        while True:
            # Receive message from client
            message = client_socket.recv(1024).decode().strip()
            if not message:
                continue  # Skip empty messages
            
            # Add message to message history
            message_history.append((username, message))
            
            # Broadcast message to all clients
            for user_socket in users:
                if user_socket != client_socket:
                    user_socket.sendall(f"{username}: {message}\n".encode())
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    
    # Remove user from dictionary and close socket
    del users[client_socket]
    client_socket.close()
    print(f"Disconnected from {client_address}")

# Function to continuously listen for client connections
def accept_clients(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Main function
def main():
    server_host = '127.0.0.1'
    server_port = 12345
    
    # Set up server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print(f"Chat server listening on {server_host}:{server_port}")
    
    # Start thread to accept client connections
    client_accept_thread = threading.Thread(target=accept_clients, args=(server_socket,))
    client_accept_thread.start()

if __name__ == "__main__":
    main()



