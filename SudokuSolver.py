from typing import List 

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [[False for _ in range(9)] for _ in range(9)]
        cols = [[False for _ in range(9)] for _ in range(9)]
        block = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]

        valid = False 

        moves = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    moves.append((i, j))
                else:
                    digit = int(board[i][j])-1
                    rows[i][digit] = True
                    cols[j][digit] = True
                    block[i//3][j//3][digit] = True


        def dfs(pos):
            nonlocal valid 
            if pos == len(moves):
                valid = True
                return 

            i, j = moves[pos] 
            for digit in range(9):
                if  rows[i][digit] == False and cols[j][digit] == False and block[i//3][j//3][digit] == False:
                    rows[i][digit] = True
                    cols[j][digit] = True
                    block[i//3][j//3][digit] = True

                    board[i][j] = str(digit + 1)

                    dfs(pos+1)

                #    board[i][j] = "."
                    rows[i][digit] = False
                    cols[j][digit] = False
                    block[i//3][j//3][digit] = False 
                
                if valid:
                    return  


        dfs(0)

        return None
        




if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]


    board1 = [[".",".","4",".",".",".","6","3","."],
             [".",".",".",".",".",".",".",".","."],
             ["5",".",".",".",".",".",".","9","."],
             [".",".",".","5","6",".",".",".","."],
             ["4",".","3",".",".",".",".",".","1"],
             [".",".",".","7",".",".",".",".","."],
             [".",".",".","5",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."]]

    Solution().solveSudoku(board)
    print(board)