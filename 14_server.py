import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create TCP socket
server_socket.bind(("127.0.0.1", 5000))
server_socket.listen(2)  # listen to socket (2 connect)
print("waiting for connection...")

conn, address = server_socket.accept()  # accept new connection
print(address, 'connected')
request = conn.recv(10).decode("ascii") # get 10 ascii characters
print('got request:',request)
while request != "":
    response = request.upper()
    conn.send(response.encode("ascii"))
    request = conn.recv(10).decode("ascii")
    print('got request:',request)