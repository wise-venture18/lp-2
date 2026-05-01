class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0]*n for _ in range(n)]

    def is_safe(self, row, col):
        # Check column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check left diagonal
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check right diagonal
        i, j = row-1, col+1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve_nq(self, row=0):
        if row == self.n:
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1

                if self.solve_nq(row + 1):
                    return True

                # Backtrack
                self.board[row][col] = 0

        return False

    def print_solution(self):
        for row in self.board:
            print(row)


# Run
n = int(input("Enter value of N: "))
q = NQueens(n)

if q.solve_nq():
    print("\nSolution:")
    q.print_solution()
else:
    print("No solution exists")
