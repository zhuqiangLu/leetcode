from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            x = abs(nums[i])

            if x <= n:
                
                nums[x-1] = -1 * (abs(nums[x-1]))
        
        print(nums)
        for i in range(n):
            if nums[i] > 0:
                return i+1
        print(nums)
        return n+1


if __name__ == "__main__":
    nums = [0,2,2,4,0,1,0,1,3]
    nums = [1,2,3,4,5,6,7,8,9,20]
    nums = [3,4,-1,1]
    nums = [1,2, 0]
    nums = [5,4,2,1]
    print(Solution().firstMissingPositive(nums))