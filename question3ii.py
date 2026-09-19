import socket

try:
    client = socket.socket()
    client.connect(("localhost", 5000))

    client.send("Hello from client!".encode())

    print("Message sent")

    client.close()

except Exception as e:
    print("Error:", e)
