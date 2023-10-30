#!/usr/bin/env python3


'''
100. Write a Python program to get the name of
the host on which the routine is running.
'''
import socket
print(f'Hostname: {socket.gethostname()}')
