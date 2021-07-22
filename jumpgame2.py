from typing import List 

class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return 0
        step = 0
        s = 0

        while True:
            
            hop = nums[s]
            step += 1

            if s + hop >= n-1:
                return step

            maxIdx = 0
            maxLen = -1 
            for i in range(1, hop+1):
                if nums[s+i] + i > maxLen:
                    maxLen = nums[s+i] + i 
                    maxIdx = s+i 
            

                     
            s = maxIdx

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    nums = [1,1,2,1,1]
    nums = [1, 3, 2]
    nums = [1,2,1,1,1]
    # nums = [4,1,1,3,1,1,1]
    print(Solution().jump(nums))