class Solution:
    
    def countAndSay(self, n: int) -> str:
        
        # say starts from 2
        s = "1"
        if n == 1:
            return s 


        def say(s):
            prev = None 
            countDict = dict()
            saying = list()
            for c in s:
                if c != prev:
                    if prev is not None:
                        saying.append(str(countDict[prev]))
                        saying.append(prev)
                    countDict[c] = 0
                
                countDict[c] += 1
                prev = c

            saying.append(str(countDict[prev]))
            saying.append(prev)
            return "".join(saying)

            
                    


        
        for _ in range(1, n):
            s = say(s)

        return s


if __name__ == "__main__":
    n = 4
    print(Solution().countAndSay(n))