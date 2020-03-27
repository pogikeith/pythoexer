

def display_board(board):
    clear_output
    print(board[7]+ ' | ' + board[8] + '|' + board[9])
    print(board[4]+ ' | ' + board[5] + '|' + board[6])
    print(board[1]+ ' | ' + board[2] + '|' + board[3])
test_board = ['#', 'x', 'o', 'x', 'o','x', 'o','x', 'o',]
display_board(test_board)