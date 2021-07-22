class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        neg = False
        if n < 0:
            x = 1/x 
            neg = True
            n *= -1



        f = 1
        res = 1
        ori = x
        flag = True
        while True:
            print(f, n)
            if f == n:
                break 
            if f + f > n:
               res *= x 
               x = ori 
               
               n -= f
               f = 1
            else:
                x *= x
                f += f
        

                
        return res * x

if __name__ == "__main__":
    print(Solution().myPow(2.1, 3))