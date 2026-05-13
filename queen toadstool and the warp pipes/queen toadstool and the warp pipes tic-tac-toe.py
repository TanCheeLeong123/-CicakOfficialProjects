import random


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board
    # (ignore index 0).
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item
    # and the computer's letter as the second.
    letter = ''

    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # First element is player's letter,
    # second is computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Given a board and player's letter,
    # this function returns True if that player has won.

    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or  # top row
        (bo[4] == le and bo[5] == le and bo[6] == le) or  # middle row
        (bo[1] == le and bo[2] == le and bo[3] == le) or  # bottom row
        (bo[7] == le and bo[4] == le and bo[1] == le) or  # left column
        (bo[8] == le and bo[5] == le and bo[2] == le) or  # middle column
        (bo[9] == le and bo[6] == le and bo[3] == le) or  # right column
        (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)     # diagonal
    )


def getBoardCopy(board):
    # Make a duplicate of the board list and return it.
    boardCopy = []

    for i in board:
        boardCopy.append(i)

    return boardCopy


def isSpaceFree(board, move):
    # Return True if the passed move is free.
    return board[move] == ' '


def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or \
            not isSpaceFree(board, int(move)):

        print('What is your next move? (1-9)')
        move = input()

    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list.
    # Returns None if no valid move exists.

    possibleMoves = []

    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Determine where the computer should move.

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # First, check if computer can win in next move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)

        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)

            if isWinner(boardCopy, computerLetter):
                return i

    # Block player's winning move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)

        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)

            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take a corner.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])

    if move is not None:
        return move

    # Try to take center.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken.

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False

    return True


print('Welcome to Queen Toadstool & The Warp Pipes Tic-Tac-Toe!')


while True:

    # Reset the board.
    theBoard = [' '] * 10

    playerLetter, computerLetter = inputPlayerLetter()

    turn = whoGoesFirst()

    print('The ' + turn + ' will go first.')

    gameIsPlaying = True

    while gameIsPlaying:

        if turn == 'player':

            # Player's turn.
            drawBoard(theBoard)

            move = getPlayerMove(theBoard)

            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You win!')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:

            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)

            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You lose!')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')

    if not input().lower().startswith('y'):
        break
