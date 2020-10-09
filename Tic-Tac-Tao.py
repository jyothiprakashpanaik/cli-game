'''
	1|2|3 
	-+-+-
	4|5|6
	-+-+-
	7|8|9
'''
import random

def display(board):
	print(f"""
{board[7]}|{board[8]}|{board[9]}                             7 | 8 | 9 
---+---+---                            ---+---+---
{board[4]}|{board[5]}|{board[6]}    -- Position -->          4 | 5 | 6 
---+---+---                            ---+---+---
{board[1]}|{board[2]}|{board[3]}                             1 | 2 | 3 
""")

def check(board):
	check = 0
	# row
	if board[1] == board[2] == board[3] != '   ' or \
	   board[4] == board[5] == board[6] != '   ' or \
	   board[7] == board[8] == board[9] != '   ':
	   check = 1
	# col
	elif board[1] == board[4] == board[7] != '   ' or \
	    board[2] == board[5] == board[8] != '   ' or \
	    board[3] == board[6] == board[9] != '   ':
	    check = 1
	# diagonal
	elif board[1] == board[5] == board[9] != '   '  or \
		 board[3] == board[5] == board[7] != '   ':
		 check = 1
	return check

def valid_input():
	while True:
		pos = input("Enter position:")
		if pos != ' ':
			try :
				if int(pos) in range(1,10):
					pos = int(pos)
					break
				print("\nNot a valid Number")
			except:
				print("Enter a Number")

		else:
			print("Thank you for Playing Tic Tac Toe!")
			exit()
	return int(pos)

def valid_pos(turn):
	print(f"{turn} chance")
	pos = valid_input()
	while True:
		print(pos)
		if board[pos] == '   ':
			board[pos] = turn
			break
		else:
			print("Cannot Overwrite, Plz Select new loc")
			pos = valid_input()

	


def userInput(board,symbol):
	sym1, sym2 = symbol[random.randint(0,1)]
	# print(sym1,sym2)
	print(f"\n\n{sym1} is going first\n")
	display(board)

	for i in range(9):
		if i%2 == 0:
			turn = ' '+sym1+' '
			valid_pos(turn)
			display(board)


		else:
			turn = ' '+sym2+' '
			valid_pos(turn)
			display(board)
		if i >= 4:

			if check(board):
				display(board)
				print(f"'{turn}' Won")
				break
		if i == 8:
			print("None Won. It's a TIE")



def main():
	global board
	board = ["Just to adjust loc :D",'   ','   ','   ','   ','   ','   ','   ','   ','   ']
	symbol = [("X","O"),("O","X")]
	again = 'y'
	while True and again == 'y':
		marker = input("\nEnter the Marker: ").upper()
		if marker == "X" or marker == "O":
			userInput(board, symbol)
			again = input("\nDo you wana play again? [y/n] ")
		else:
			print("plz enter a correct marker (X,O)")	
		# display(board)
	print("Thank you for Playing My game.")
	
main()