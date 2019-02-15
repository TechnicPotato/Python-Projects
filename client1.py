import sys
import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 50005
MESSAGE = b"Hello, World!"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if len(sys.argv)>1:
    sock.sendto(sys.argv[1].encode(), (UDP_IP, UDP_PORT))
    #argv
else:
    print("missing commandline parameter!")
