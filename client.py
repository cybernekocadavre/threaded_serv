#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import socket
import sys

def echo_client(message):
    server_host = '127.0.0.1'
    server_port = 12345

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))

    # Send the message to the server
    client_socket.sendall(message.encode())

    # Receive data from the server
    data = client_socket.recv(1024)
    print("Received:", data.decode())

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    # Check if a message is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python client.py <message>")
        sys.exit(1)

    message = sys.argv[1]
    echo_client(message)


