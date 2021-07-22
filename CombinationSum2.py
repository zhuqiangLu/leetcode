from typing import List 

class Solution:
    def helper(self, candidates, target):
        if len(candidates) == 0:
            return None 
        
        elif candidates[0] > target:
            return None 

        
        
        else:
            res = list()
            visited = dict()
            for i in range(len(candidates)):
                if visited.get(candidates[i]) is None:
                    visited[candidates[i]] = True

                if visited[candidates[i]]:
                    if candidates[i] == target:
                        res.append([candidates[i]])
                    elif candidates[i] < target:
                        com = self.helper(candidates[i+1:], target-candidates[i])
                        if com is not None:
                            
                            for c in com:
                                res.append([candidates[i]] + c)
                    visited[candidates[i]] = False
            return res

        
    def combinationSum2(self, candidatess: List[int], target: int) -> List[List[int]]:
        candidates.sort()   
        
        return self.helper(candidates, target) 
if __name__ == "__main__":
    candidates = [2,5,2,1,2]
    target = 5
    print(Solution().combinationSum2(candidates, target))

