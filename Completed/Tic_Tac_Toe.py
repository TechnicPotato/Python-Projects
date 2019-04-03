# Needs to be done this way otherwise identical list creation
board = []
for i in range(0,3):
	board.append([" "] * 3) 

def printboard():
	print(board[0][0] + "|" + board[1][0] + "|" + board[2][0])
	print("-" *5)
	print(board[0][1] + "|" + board[1][1] + "|" + board[2][1])
	print("-" *5)
	print(board[0][2] + "|" + board[1][2] + "|" + board[2][2])
	
def winner(n):
	return ((board[0][0] == board[0][1] == board[0][2] == n) or #Top Row
			(board[1][0] == board[1][1] == board[1][2] == n) or #Second Row
			(board[2][0] == board[2][1] == board[2][2] == n) or #Third Row
			#Second set of conditions
			(board[0][0] == board[1][0] == board[2][0] == n) or
			(board[0][1] == board[1][1] == board[2][1] == n) or
			(board[0][2] == board[1][2] == board[2][2] == n) or
			#Diagonals
			(board[0][0] == board[1][1] == board[2][2] == n) or
			(board[0][2] == board[1][1] == board[2][0] == n))
def full():
	for i in board:
		for b in i:
			if b == " ":
				return False
	else:
		return True
		
#Toggle for X or O, X = 0 , 0 = 1
i = 0
while True:
	move_string = input("")
	if [c.isnumeric() for c in move_string.split(" ")] == [True,True]:
		move = [int(c) for c in move_string.split(" ")]
		if i == 0:
			if board[move[0]][move[1]] == " ":
				board[move[0]][move[1]] = "X"
				i = 1
				if winner("X"):
					print("X wins!")
					break
				elif full():
					print("Draw")
					break
			else:
				print("Invalid input")
				pass
		else:
			if board[move[0]][move[1]] == " ":
				board[move[0]][move[1]] = "O"
				i = 0
				if winner("O"):
					print("O wins!")
					break
				elif full():
					print("Draw")
					break
			else:
				print("Invalid input")
				pass
		print()
		printboard()
		print()
	else:
		print("Invalid input")
		pass
print()
printboard()
print()
	
