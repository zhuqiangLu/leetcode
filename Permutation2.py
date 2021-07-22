from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        

        n = len(nums)
        res = list()
        vis = [False for _ in range(n)]
        nums.sort()
        def backtrack(perm):

            if len(perm) == n:
                print(len(perm), perm)
                res.append(perm.copy())
            else:
                for i in range(n):
                    if vis[i] or (i > 0 and nums[i] == nums[i-1] and not vis[i-1]):
                        continue
                    else:
                        vis[i] = True
                        perm.append(nums[i])
                        backtrack(perm)
                        perm.pop(-1)
                        vis[i] = False 
        
        backtrack([])
        return res

        