from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        # print(target)
        candidates.sort()
        if candidates[0] > target:
            return res 
        for can in candidates:
            if can == target:
                res.append([can])

        for i in range(len(candidates)):
            can = candidates[i] 
            tmps = self.combinationSum(candidates[i:], target-can)

            if len(tmps) == 0:
                continue
            for tmp in tmps:
                res.append(tmp + [can])

        return res

if __name__ == "__main__":
    candidates = [2,3,5]
    target = 8
    print(Solution().combinationSum(candidates, target))
