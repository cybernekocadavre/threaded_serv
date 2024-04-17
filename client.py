#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# client.py

import socket
import sys

def echo_client():
    server_host = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    username_prompt = client_socket.recv(1024).decode()
    print(username_prompt, end="")
    
    username = input()
    client_socket.sendall(username.encode())

    while True:
        message = input("Введите сообщение : ")
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print("Received:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    echo_client()
