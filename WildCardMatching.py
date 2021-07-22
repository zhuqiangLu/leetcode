class Solution:
    def isMatch(self, s:str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]

        dp[0][0] = True
        for i in range(1, m+1):
            if p[i-1] == "*":
                dp[i][0] = True 
            else:
                break
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                
        for d in dp:
            print(d)

        return dp[m][n]



if __name__ == "__main__":
    s = "a"
    p = "*a"
    print(Solution().isMatch(s, p))