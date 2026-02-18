import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind (("127.0.0.1",5000))
server_socket.listen(1)


print ("server waiting for the connection...")

conn,addr = server_socket.accept()
print("connect to:",addr)


data= conn.recv(1024).decode()
print("client says:",data)

conn.send("Hello from server".encode())

conn.close()
server_socket.close()