import socket

connection = socket.create_connection(('127.0.0.1',1024)) # Assuming CS server on localhost port 1024
connection.sendall(b'kent\x00harry\x00test\x00')
response = connection.makefile()
print(response.readline())