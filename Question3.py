import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Waiting for client...")

try:
    connection, address = server.accept()
    message = connection.recv(1024).decode()
    print("Message:", message)
    connection.close()
except:
    print("Connection error")

server.close()
