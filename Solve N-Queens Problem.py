def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q' or \
               (col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q') or \
               (col + (row - i) < n and board[i][col + (row - i)] == 'Q'):
                return False
        return True

    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    board = [['.'] * n for _ in range(n)]
    result = []
    backtrack(0)
    return result

# Example
print(solve_n_queens(4))
