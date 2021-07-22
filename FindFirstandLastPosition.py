from typing import List


class Solution:
    

    def search(self, nums, left, right, target):
        n = len(nums)
        if n == 0:        
           return [-1, -1]
        if left > right:
            return [-1, -1]
        if nums[0] == target and nums[-1] == target:
            return [0, n-1]


        if target < nums[left] or target > nums[right]:
            return [-1, -1]
        
            
        res = list()
        while left <= right:
            mid = (left + right) // 2

            midNum = nums[mid]

            if midNum < target:
                left = mid + 1
            elif midNum > target:
                right = mid - 1
            else:
                leftStart, leftEnd = self.search(nums, left, mid-1, target)
                rightStart, rightEnd = self.search(nums, mid+1, right, target)
                if leftEnd != -1:                        
                    res.append(leftStart)
                else:
                    res.append(mid)
                
                if rightEnd != -1:
                    res.append(rightEnd)
                else:
                    res.append(mid)

                return res 

        return [-1, -1]                

        


    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        if n == 0:
           return [-1, -1]
        


        left = 0
        right = n-1 

        res = self.search(nums, left, right, target)
        print(res)





if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    nums = [1, 4]
    
    target = 4
    print(Solution().searchRange(nums, target))

















        
