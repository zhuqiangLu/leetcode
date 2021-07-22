class Solution:
    def isNumber(self, s: str) -> bool:
        if s == "":
            return False 
        
        l = ord('0')
        r = ord('9')
        
        def removeSign(s):
            if len(s) == 0:
                return s 
            if s[0] == "+" or s[0] == "-":
                return s[1:]
            else:
                return s


        def isValid(s, isDecimal = False):
            # no sign no e
            
            if len(s) == 0:
                return False
            
            if len(s) == 1 and s == '.':
                return False
            counter = 0
            for c in s:
                if ord(c) >= l and ord(c) <= r:
                    continue 
                elif c == '.':
                    if isDecimal:
                        counter += 1
                        if counter > 1:
                            return False 
                    else:
                        return False
                else:
                    return False         
            return True 


        beforeE = None
        afterE = None 

        hasE = False
        for i in range(len(s)):
            c = s[i] 
            if c == 'e' or c == 'E':
                hasE = True 
                beforeE = removeSign(s[:i])
                afterE = removeSign(s[i+1:])
        

        if hasE: 
            return isValid(beforeE, isDecimal=True) and isValid(afterE)
        
        else:
            return isValid(removeSign(s), isDecimal=True)
        



            

if __name__ == "__main__":
    s = "+3e-3"
    s = '-123.456e789'
    s = '--6'
    s = '95a54e53'
    print(Solution().isNumber(s))