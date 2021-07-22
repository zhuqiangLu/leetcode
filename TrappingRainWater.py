from typing import List
class Solution:
    def dp(self, height):
        n = len(height)
        leftMax = [0 for _ in range(n)]
        rightMax = [0 for _ in range(n)]

        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]

        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i-1])
        
        for i in range(n-2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])

        
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res


    def trap(self, height: List[int]) -> int:
        res  = self.dp(height) 
        return res

        


if __name__ == "__main__":
    heights = [0, 1,0,2,1,0,1,3,2,1,2,1]
    heights = [4,2,0,3,2,5]
    # heights = [2, 0, 2]
    print(Solution().trap(heights))