class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        def swap(s, e, nums):
            # nums is in ascd order 
            # print(s, e)
            head = nums[:s] 
            left = [nums[s]]
            mid = nums[s+1:e]
            right = [nums[e]]
            tail = nums[e+1:]

            return head + right + left + mid + tail
        factorials = [1 for _ in range(1 + n)]
        nums = [str(i + 1) for i in range(n)]
        

        for i in range(1, n+1):
           factorials[i] = i * factorials[i - 1]

        factorials[0] = 0 
        
        print(factorials) 
        
        while k > 0:
            s = 0
            for i in range(1, n+1):
                if k > factorials[i-1] and k <= factorials[i]:
                    s = n - i
                    break 

            if s == n - 1:
                break
            
            # calculate which num to be swap 
            e = s 
            
            while k > factorials[n - s - 1]:
                k -= factorials[n - s - 1]
                e += 1
            
            nums = swap(s, e, nums)
        
        return "".join(nums)
            



    

if __name__ == "__main__":
    n = 5
    k = 11
    print(Solution().getPermutation(n, k))