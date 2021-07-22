class Solution:
   
   
    def threeSum(self, nums):

        if len(nums) < 3:
            return [] 

        
        nums.sort()
        
        res = list()
        for i in range(len(nums)):
            if nums[i] > 0:
                return res 
            
            # ignore the duplicated one 
            if i > 0 and nums[i-1] == nums[i]:
                continue 

            # inner loop
            l = i+1
            r = len(nums)-1
            while r > l:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    while (l < r) and nums[l] == nums[l+1]:
                        l += 1
                    while (l < r) and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                    l += 1
                
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
            


            
        
            
        return res  


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    res = Solution().threeSum(nums)
    print(res)
