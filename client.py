#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# client.py

import socket
import sys

def echo_client():
    server_host = '127.0.0.1'
    server_port = 12345

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))

    # Receive username prompt from the server
    username_prompt = client_socket.recv(1024).decode()
    print(username_prompt, end="")
    
    # Input username and send to server
    username = input()
    client_socket.sendall(username.encode())

    # Continuous sending of messages
    while True:
        message = input("Enter your message: ")
        client_socket.sendall(message.encode())

        # Receive and print data from the server
        data = client_socket.recv(1024)
        print("Received:", data.decode())

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    echo_client()
