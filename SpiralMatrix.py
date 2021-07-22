from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        res = list()

        total = 0

        ci, cj = 0, -1
        si, sj = 0, 0

        rowE = m-1
        colE = n-1
        rowS = 0 
        colS = 0

        start = True
        left, right, down, up = True, False, False, False
        while total < n * m:
            
            
            if left:
                cj += 1
                if cj == colE:
                    left = False
                    down = True

            elif right:
                cj -= 1
                if cj == colS:
                    right = False 
                    up = True 

            elif down:
                ci += 1
                if ci == rowE:
                    down = False 
                    right = True
            elif up:
                ci -= 1
                if ci == rowS:
                    up = False
                    left = True 
            
            print(ci, cj, left, right, up, down, start)
            # reach stating
            if ci == si and cj == sj:
                if not start:
                    print('inner', rowS, rowE, colS, colE)
                    rowS += 1
                    colS += 1
                    rowE -= 1
                    colE -= 1
                    si += 1
                    sj += 1
                    ci = si 
                    cj = sj-1
                    start = True
                    up = False 
                    left = True
                else:
                    start = False
                    res.append(matrix[ci][cj])
                    total += 1
                
            else:
                res.append(matrix[ci][cj])
                total += 1
        return res
                

        
            
            
            



if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))