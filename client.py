#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

def echo_client():
    server_host = '127.0.0.1'
    server_port = 12345
    message = "Enter message"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_host, server_port))

    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print("Received:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    echo_client()

