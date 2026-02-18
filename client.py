import socket

client_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect (("127.0.0.1",5000))

client_socket.send("Hello server".encode())

data= client_socket.recv(1024).decode()
print("server says:",data)

client_socket.close()