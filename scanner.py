#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import socket

def port_scanner(host):
    print(f"Проверяем порты {host}...")
    for port in range(1, 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Порт {port} открыт")
                s.close()
        except socket.error:
            print("Подключение к серверу невозможно.")
            break

if __name__ == "__main__":
    host = input("Введите IP или имя хоста: ")
    port_scanner(host)
