import sys
import socket
HOST = '127.0.0.1'
PORT = 65432
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
if len(sys.argv)>1:
    sock.sendall(sys.argv[1].encode())
    data = sock.recv(1024)
    print('Received', data.decode())
else:
    print("missing commandline parameter!")