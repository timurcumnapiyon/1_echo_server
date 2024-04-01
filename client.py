import socket

host = input("Enter server hostname or IP address: ")
port = int(input("Enter server port: "))

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

while True:
    msg = input("Your string (type 'exit' to quit): ")
    sock.send(msg.encode())
    if msg.strip() == 'exit':
        break
    data = sock.recv(1024)
    print(data.decode())
sock.connect((host, port))

msg = input("Enter your message: ")
sock.send(msg.encode())

data = sock.recv(1024)
print(data.decode())

sock.close()
