import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 50005
MESSAGE = b"Hello, World!"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  """Creates a new socket using family, socket type and protocol number
AF_INET is an address family  requiring (hostname(IP), port). SOCK_DGRAM represents socket types
network socket types: DGRAM represents datagram: connectionless point for data packets, each packet being individually addressed and router.
Stream representing connection orientated sequenced data, used for stuff not requiring speed and requiring specific ordering (file transfer)"""
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
