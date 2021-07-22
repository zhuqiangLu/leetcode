class Solution:
    def dp(self, s: str) -> int:
        # dp[i] -> the longest valid parentheses from 0 to i 
        n = len(s) 
        dp = [0 for _ in range(n+1)]

        maxLen = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2

                # if s[i-1] is ")", then s[i-1-dp[i-1]] may also be "("
                elif s[i-1] == ")":
                    left = i - 1 - dp[i-1]

                    if left >= 0 and s[left] == "(":
                        if left > 1:
                            dp[i] = dp[i-1] + 2 + dp[left-1]
                        else:
                            dp[i] = dp[i-1] + 2
                if dp[i] > 0:
                    maxLen = max(maxLen, dp[i])
        
        return maxLen
    def stack(self, s: str) -> int:
        stack = list() 
        stack.append(-1)
        maxLen = 0
        for i in range(len(s)):
            if s[i] == "(" and len(stack) > 0:
                stack.append(i)
            elif s[i] == ")":
                stack.pop(-1)
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i-stack[-1])
        return maxLen 

    def twoPointer(self, s: str) -> int:
        left = 0 
        right = 0            
        maxLen = 0
        for i in range(len(s)):
            c = s[i]

            if c == "(":
                left += 1
            else:
                right += 1

            if left < right:
                left = 0 
                right = 0 

            if left == right:
                maxLen = max(right, maxLen)             

            print(c, left, right, maxLen)

        i = len(s)-1
        left = 0 
        right = 0
        print(maxLen)
        while i > -1:

            c = s[i]
            if c == "(":
                left += 1
            else:
                right += 1
            
            if left > right:
                left = 0
                right = 0
            if left == right:
                maxLen = max(left, maxLen)
            i -= 1
        return maxLen*2



    def longestValidParentheses(self, s: str) -> int:

        return self.twoPointer(s), self.stack(s)


                   

                


if __name__ == '__main__':
    s =  ")(((((()())()()))()(()))("
    # s = "()(()"
    s = "((()))())"
    s = "()()"
    print(Solution().longestValidParentheses(s))