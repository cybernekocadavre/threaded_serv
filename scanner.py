#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import socket

def port_scanner(host):
    print(f"Scanning ports on {host}...")
    for port in range(1, 65536):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port} is open")
                s.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except socket.error:
            print("Couldn't connect to server.")
            break

if __name__ == "__main__":
    host = input("Enter the hostname or IP address to scan: ")
    port_scanner(host)
