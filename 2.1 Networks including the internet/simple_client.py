import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 60000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected.  Sending a message...")
    s.sendall("I love you Server!".encode("ASCII"))
    data = s.recv(1024)

print('Received from Server:', data.decode("ASCII"))