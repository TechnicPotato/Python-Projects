#FileCopy
import sys
if len(sys.argv) == 3:
    """This section reads the code and writes it to data"""
    copy = open(sys.argv[1], mode = 'r+b') #Copied Data is Binary and in Read mode.
    data = copy.read()
    copy.close()
    """This section takes the data and writes it to argv[2]"""
    destination = open(sys.argv[2], mode = 'w+b')
    destination.write(data)
    destination.close()
else:
    print("Error")
