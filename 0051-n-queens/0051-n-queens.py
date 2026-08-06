class Solution(object):

    def backtrack(self, row, n, board, cols, diag1, diag2, ans):

        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for col in range(n):

            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            self.backtrack(row + 1, n, board, cols, diag1, diag2, ans)

            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    def solveNQueens(self, n):

        board = [["."] * n for _ in range(n)]
        ans = []

        cols = set()
        diag1 = set()
        diag2 = set()

        self.backtrack(0, n, board, cols, diag1, diag2, ans)

        return ans