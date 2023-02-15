#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Jacob Miesner
    Missouri University of Science and Technology
    CS 3610
    Project 01
    9 Feb 2023
Run with the following command line parameters:
python3 client_browser.py hostname port file

Examples:
$ python3 client_browser.py info.cern.ch 80 ""
$ python3 client_browser.py localhost 6789 "hello_world.html"
"""

import sys
import socket

if len(sys.argv) != 4:
    server_hostname = "localhost"
    server_ip = "127.0.0.1"
    server_port = 6789
    file_name = "web_files/hello_world.html"
else:
    # Dele the pass and do your arg parsing here
    # Hint, you may need to get an IP from a hostame.
    server_hostname = sys.argv[1]
    server_port = int(sys.argv[2])
    file_name = sys.argv[3]
    server_ip = socket.gethostbyname(server_hostname)

try:
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # Delete the pass and make your GET request here
    client_socket.connect((server_hostname, server_port))
    request = "GET /" + file_name + " HTTP/1.1\r\n" + "Host: " + server_hostname + "\r\n\r\n"
    client_socket.send(request.encode())

    # Delete the pass and parse the return data here
    # Hint: a loop helps to make sure you got all the data
    # Just print what's returned from the server
    data = client_socket.recv(1024).decode()
    print(data)

except Exception as e:
    print("Exception was: ", e)

finally:
    client_socket.close()
