from typing import List

class Solution:
    def search(self, nums: List[int], target:  int) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = 0
        while left < right:
            
            leftNum = nums[left]
            rightNum = nums[right]
            mid = int((left + right)/2)
            midNum = nums[mid]
            if leftNum > midNum:
                right = mid
            elif rightNum < midNum:
                left = mid 
            else:
                mid = 0
                break
            if leftNum == midNum or rightNum == midNum:
                mid = left if leftNum < rightNum else right
                break

        offset = len(nums) - mid 
        
        left = 0 
        right = len(nums) - 1
        
        def getIdx(idx):
            idx -= offset 
            if idx < 0:
                idx += len(nums)       
            return idx

        while left <= right:

            leftNum = nums[getIdx(left)]
            rightNum = nums[getIdx(right)]
            mid = int((left + right)/2) 
            midNum = nums[getIdx(mid)]
            # print(left, right, mid, leftNum, rightNum, midNum)
            if midNum == target:
                return getIdx(mid)
            
            elif midNum < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
            
        
        
                

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    nums = [1, 3, 5]
    print(Solution().search(nums, 0))