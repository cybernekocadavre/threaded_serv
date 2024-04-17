#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

def chat_client():
    server_host = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    try:
        # Receive prompt for username
        data = client_socket.recv(1024)
        print(data.decode(), end='')
        username = input()
    
        # Send username to the server
        client_socket.sendall(username.encode())
    
        while True:
            # Prompt user for message
            message = input("Enter your message: ")
            if not message:
                break  # Exit loop if message is empty
    
            # Send message to the server
            client_socket.sendall(message.encode())
    
            # Receive and print messages from the server
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break  # Exit inner loop if no more data
                print("Received:", data.decode(), end='')  # Print received message without newline
    
            # Prompt user for a new message
            print("Enter your message: ", end='', flush=True)  # Flush the buffer to ensure prompt is shown immediately
except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Close the connection
    client_socket.close()


if __name__ == "__main__":
    chat_client()


