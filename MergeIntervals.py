from typing import List 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = list()
        for s,e in intervals:
            if len(res) == 0:
                res.append([s, e])
            else:
                if s <= res[-1][1]:
                    res[-1][1] = max(e, res[-1][1])
                else:
                    res.append([s, e])

        return res
            



if __name__ == "__main__":
    intervals = [[1,3],[8, 10], [2,6],[15,18]]
    print(Solution().merge(intervals)) 