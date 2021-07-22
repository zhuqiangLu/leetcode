from typing import List 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) ->List[List[int]]:
        
        res = list()
        for i in range(len(intervals)):
            if intervals[i][0] < newInterval[0]:
                res.append(intervals[i])
            else:
                res.append(newInterval)
                res += intervals[i:]
                break

        if len(res) == len(intervals):
            res.append(newInterval)
        
        
        

        
        ans = list()
        for s,e in res:
            if len(ans) == 0:
                ans.append([s, e])
            else:
                if s <= ans[-1][1]:
                    ans[-1][1] = max(e, ans[-1][1])
                else:
                    ans.append([s, e])
        return ans


if __name__ == "__main__":
    # intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [2,7]
    intervals = [[1,5]]
    # newInterval = []
    print(Solution().insert(intervals, newInterval))