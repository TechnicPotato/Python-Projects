import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 50005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
	data, addr = sock.recvfrom(1024) #1024 bit message
	print ("received message:", data.decode())
	if (data==b"stop"):
		break
