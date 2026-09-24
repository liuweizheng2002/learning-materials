



import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("192.168.1.199", 6666))

with open('d:/Trae_test/test.txt', 'rb') as src_f:
    while True:
        data = src_f.read(8192)
        client_socket.send(data)
        if len(data) == 0:
            break



client_socket.close()





