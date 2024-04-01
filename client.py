import socket

host = input("Enter server hostname or IP address: ")
port = int(input("Enter server port: "))

sock = socket.socket()
sock.connect((host, port))

msg = input("Enter your message: ")
sock.send(msg.encode())

data = sock.recv(1024)
print(data.decode())

sock.close()
