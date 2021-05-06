theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(f"{board['top-L']}  | {board['top-M']} | {board['top-R']}")
    print(f'---+---+---')
    print(f"{board['mid-L']}  | {board['mid-M']} | {board['mid-R']}")
    print(f'---+---+---')
    print(f"{board['low-L']}  | {board['low-M']} | {board['low-R']}")


turn = 'X'
for i in range(9):
  printBoard(theBoard)
  move = input(f'Turn for {turn}. Which space: ')
  theBoard[move] = turn
  if turn == 'X':
      turn = 'O'
  else:
      turn = 'X'

printBoard(theBoard)
