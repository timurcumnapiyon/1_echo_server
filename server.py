import socket

def find_free_port(start_port):
    port = start_port
    while True:
        try:
            sock = socket.socket()
            sock.bind(('', port))
            print(f"Server is listening on port {port}")
            return sock, port
        except OSError:
            print(f"Port {port} is already in use, trying the next one...")
            port += 1

sock, port = find_free_port(9090)
sock.listen(0)
conn, addr = sock.accept()
print("Client accepted")
print("Client address:", addr[0])
print("Client port:", addr[1])

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()
