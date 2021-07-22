from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        dist = 0

        for i in range(n-1):

            if i <= dist:
                dist = max(i + nums[i], dist)
        
        print(dist)
        if dist >= n-1:
            return True 
        else:
            return False
            


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    nums = [3,2,1,0,4]
    nums = [0, 2, 3]
    print(Solution().canJump(nums))
        