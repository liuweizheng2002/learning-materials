



import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("192.168.1.199", 6666))

server_socket.listen(5)

accept_socket, client_info = server_socket.accept()

with open('../data/my.txt','wb') as dest_f:

    while True:
        bys = accept_socket.recv(8192)
        if len(bys) == 0:
            break
        dest_f.write(bys)

accept_socket.close()


