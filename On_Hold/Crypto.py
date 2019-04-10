import codecs, base64, binascii
#Hex to Base64 converted
#Converter 1 -> Converts from String to string, then to byte then to
def hh(message):
	a = codecs.decode(message, 'hex') #Returns a string
	b = codecs.encode(a,'base64') #Convert to Base64, and returns a byte.
	rmessage = b.strip().decode('ascii') #Convert string to ASCII and strips the b and trailing newline
	print(rmessage)
#Original decoded message is type 'byte' and hence has a trailing newline and header
#Converter 2 -> Converts to B64 as a byte at all times:
def h64(message):
	asciimessage = binascii.unhexlify(message)
	return base64.b64encode(asciimessage)
#Fixed XOR decoder
def convord(message):
	rlist = []
	rlist.append((ord(c)) for c in message)
	print(rlist)
convord("potato")
def XOR(a, b):
	#Convert message 1 and 2 to unicode

XOR("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965")
