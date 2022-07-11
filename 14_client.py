import socket

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 5000))

request = input("to server:")
while request != 'quit':
    client_socket.send(request.encode("ascii"))
    response = client_socket.recv(10).decode("ascii")
    print('from server:', response)
    request = input("to server:")

client_socket.close()