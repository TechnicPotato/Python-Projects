import codecs
#Hex to Base64 converted
def hb64(message):
	a = codecs.encode(codecs.decode(message, 'hex'), 'base64').decode()
	print(a) 
def hh(message):
	a = codecs.decode(message, 'hex')
	b = codecs.encode(a,'base64')
	print(b)
#Why are there two junk letters in front and behind