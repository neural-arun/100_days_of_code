# Here is the starting Tic-Tac-Toe board
row1 = ["X", " ", " "]
row2 = [" ", "X", " "]
row3 = [" ", " ", " "]
board = [row1, row2, row3]

print("Player O's turn.")
print(f"{row1}\n{row2}\n{row3}")

# Get input from the user for their move
move = input("Where do you want to place your 'O'? ")

# 🔽 YOUR CODE GOES BELOW THIS LINE 🔽
letter = move[0].lower()
abc = ["a","b","c"]
column_index = abc.index(letter)
row_index = int(move[1]) - 1
board[row_index][column_index] = "O"


# 🔼 YOUR CODE GOES ABOVE THIS LINE 🔼


# Don't change the code below! It prints the final board.
print("Board updated!")
print(f"{row1}\n{row2}\n{row3}")