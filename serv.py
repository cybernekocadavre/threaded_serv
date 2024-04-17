#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import socket
import threading
import sys

def echo_server(client_socket, client_address):
    print(f"Connected to {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from {client_address}: {data.decode()}")
        client_socket.sendall(data)
    print(f"Disconnected from {client_address}")
    client_socket.close()

def handle_client_connections(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        client_thread = threading.Thread(target=echo_server, args=(client_socket, client_address))
        client_thread.start()

def main():
    server_host = '127.0.0.1'
    server_port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print(f"Server listening on {server_host}:{server_port}")

    client_handler_thread = threading.Thread(target=handle_client_connections, args=(server_socket,))
    client_handler_thread.start()

if __name__ == "__main__":
    main()

