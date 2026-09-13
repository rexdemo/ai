import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_winner(board):
    if is_winner(board, 'X'):
        return 'X'
    if is_winner(board, 'O'):
        return 'O'
    return None

def evaluate(board):
    winner = get_winner(board)

    if winner == 'X':
        return 1
    if winner == 'O':
        return -1
    if is_full(board):
        return 0

    return None

def minimax(board, alpha, beta, maximizing):
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    value = minimax(board, alpha, beta, False)
                    board[i][j] = ' '

                    best = max(best, value)
                    alpha = max(alpha, value)

                    if beta <= alpha:
                        break

        return best

    best = math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                value = minimax(board, alpha, beta, True)
                board[i][j] = ' '

                best = min(best, value)
                beta = min(beta, value)

                if beta <= alpha:
                    break

    return best

def find_best_move(board):
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                value = minimax(board, -math.inf, math.inf, False)
                board[i][j] = ' '

                if value > best_value:
                    best_value = value
                    best_move = (i, j)

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            move = find_best_move(board)
            print("Computer plays X at position:", move)
        else:
            move = tuple(map(int, input("Enter your move (row column): ").split()))

        if board[move[0]][move[1]] != ' ':
            print("Invalid move. Try again.")
            continue

        board[move[0]][move[1]] = current_player

        winner = get_winner(board)

        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
