from random import randint
from time import sleep
board = []
for i in range(0,20):
  board.append(" ")
    
while True:
    for i in range(0,20):
        if randint(0,2) == 0:
            board[i] = "*"
        else:
            board[i] = " "
    sleep(0.1)
    print(" ".join(board))


