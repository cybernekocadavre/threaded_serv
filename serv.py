#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import socket
import threading
import sys

clients = {}
message_history = []

def echo_server(client_socket, client_address, username):
    print(f"Подключились к {client_address} под ником {username}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = f"{username}: {data.decode()}"
        print(f"Получено от {client_address}: {message}")
        
        message_history.append(message)
        
        for client in clients.values():
            client.sendall(message.encode())
            
    print(f"Отключились от {client_address} под ником {username}")
    client_socket.close()
    del clients[username]

def handle_client_connections(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Новое подключение от {client_address}")
        
        client_socket.sendall("Введите ник: ".encode())
        username = client_socket.recv(1024).strip().decode()
        
        clients[username] = client_socket
        
        # Создание нового потока
        client_thread = threading.Thread(target=echo_server, args=(client_socket, client_address, username))
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






