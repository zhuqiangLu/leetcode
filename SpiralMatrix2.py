from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        total = 0
        res = [[0 for _ in range(n)] for _ in range(n)]

        l, r, t, b = 0, n-1, 0, n-1
        while total < n * n:
            # print(total)
            # right
            for i in range(l, r+1):
                total += 1
                res[t][i] = total
            t += 1
            
            # down
            for i in range(t, b+1):
                total += 1
                res[i][r] = total 
            r -= 1

            # left
            for i in range(r, l-1, -1):
                total += 1
                res[b][i] = total 
            b -= 1

            # up
            for i in range(b, t-1, -1):
                print(i, l)
                total += 1
                res[i][l] += total
            l += 1
        
        return res






            





if __name__ == "__main__":
    n = 3 
    print(Solution().generateMatrix(n))