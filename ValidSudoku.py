from typing import List 


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = dict()
        colDict = dict()

        for i in range(9):
            rowDict[i] = [0 for _ in range(10)]
            colDict[i] = [0 for _ in range(10)]
        
        r = 0
        c = 0 
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                # sub grid 
                    
                subGrid = [0 for _ in range(10)]
                
                for i in range(3):
                    for j in range(3):                            
                        
                        entry = board[r+i][c+j]

                        if entry != ".":
                            # if c+j == 4:
                            #     print(r+i, c+j)
                            entry = int(entry)
                            subGrid[entry] += 1
                            rowDict[r+i][entry] += 1
                            colDict[c+j][entry] += 1
                            if rowDict[r+i][entry] > 1\
                                    or colDict[c+j][entry] > 1\
                                        or subGrid[entry] > 1:
                                
                                return False 
                            
                                                      
                    
            
                    

        # print(colDict)
        return True






if __name__ == "__main__":
    board = [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]


    board = [[".",".","4",".",".",".","6","3","."],
             [".",".",".",".",".",".",".",".","."],
             ["5",".",".",".",".",".",".","9","."],
             [".",".",".","5","6",".",".",".","."],
             ["4",".","3",".",".",".",".",".","1"],
             [".",".",".","7",".",".",".",".","."],
             [".",".",".","5",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."]]
    print(Solution().isValidSudoku(board))
