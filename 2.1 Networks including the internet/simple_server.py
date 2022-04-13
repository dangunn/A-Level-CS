import socket

HOST = '127.0.0.1'  # This is a special IP address meaning local host (my own computer)
PORT = 60000        # ports > 1023 are safe to use

# socket.AF_INET means internet
# socket.SOCK_STREAM means TCP (SOCK_DGRAM is for UDP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
          s.bind((HOST, PORT))
          s.listen()
          print("Waiting for connection...")
          conn, addr = s.accept()
          print("connection accepted...")
          with conn:
                    print('Connected by', addr)
                    while True:
                              data = conn.recv(1024)
                              if not data:
                                        break
                              print("Received from client:", data.decode("ASCII"))
                              conn.sendall("I love you too!".encode("ASCII"))