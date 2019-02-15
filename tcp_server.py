import socket
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print('From Client', repr(data))
    data1 = list(data)
    print(data1)
    for i in range(len(data1)):
        data1[i]+=1
        data[i] %= 256
    conn.sendall(str(data1).encode())
