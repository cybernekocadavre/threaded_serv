#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import sys

def chat_client(username, message):
    server_host = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_host, server_port))

    # Send username to the server
    client_socket.sendall(username.encode())

    # Receive username prompt from the server
    data = client_socket.recv(1024)
    print(data.decode())

    # Send message to the server
    client_socket.sendall(message.encode())

    # Receive and print response from the server
    data = client_socket.recv(1024)
    print("Received:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <username> <message>")
        sys.exit(1)

    username = sys.argv[1]
    message = sys.argv[2]
    chat_client(username, message)



