from typing import List
import sys
# sys.setrecursionlimit(150000)
class Solution():
    

    def solveNQueens(self, n: List) -> List[List[str]]:            
        
        res = list()
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        moves = list()
        for i in range(n):
            for j in range(n):
                moves.append((i, j))
        queen = 0

        visited = list()

        def dfs(moves, row):                
            nonlocal queen 
            nonlocal visited

            if len(moves) == 0:
                
                if queen == n:
                    res.append(["".join(b) for b in board])
                    
                    
            
            else:
                
                
                for t in moves:
                    
                    
                    
                    i, j = t

                    if i != row:
                        continue
                    
                    tmp = list()

            
                    for k in range(len(moves)):
                        r, c = moves[k]
                        if not (r == i or c == j or abs(r-i) == abs(c-j)):
                            tmp.append((r, c))

                    
                
                    board[i][j] = 'Q'
                    queen += 1 
                    

                    dfs(tmp, row+1)

                    board[i][j] = '.'
                    queen -= 1
                    if i == 0:
                        visited.append((i,j))
                    
        dfs(moves, 0)
        return res

                

            
if __name__ == "__main__":
    n = 5
    print(Solution().solveNQueens(n))
                

