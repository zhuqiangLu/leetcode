class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()

        diff = 1e5

        ans = 0
        for i in range(len(nums)):
            
            
            if i > 0 and nums[i-1] == nums[i]:
                continue 
            
            
            l = i+1
            r = len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                else:
                    if diff > abs(target-(nums[i] + nums[l] + nums[r])):
                        diff = abs(target-(nums[i] + nums[l] + nums[r]))
                        ans = target-(nums[i] + nums[l] + nums[r])

                    if nums[i] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
       
        return target-ans



if __name__ == "__main__":
    nums = [1,1,-1,-1,3]
    target = -1
    res = Solution().threeSumClosest(nums, target)
    print(res)