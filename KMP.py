class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def findNext(pat):
            # nex[i] mean the longgest prefix == suffix before i-th char in pat
            patLen = len(pat)

        

            k = -1
            j = 0 

            nex = [0 for _ in range(patLen)]
            nex[0] = -1
            while j < patLen-1:
                
                if k == -1 or pat[j] == pat[k]:
                    # k = -1 -> initial case, 
                    # the longgest suffix prefix in pat[0] is 0
                    # as if mismatch happens at sec char in the pat, we need to compare the curr char in haystack with pat[0]
                    
                    j += 1
                    k += 1
                    nex[j] = k 
                else:
                    # cannot increment the longgest suffix and prefix as there is mismatch
                    # so, compare the last char with the longgest prefix and suffix  before k-th char \
                    # example: ABACDEABAB
                    # when j = 9, k = 3, mismatch
                    # nex for ABAC is [-1, 0, 0, 1], nex[k] points to the longgest prefix and suffix in ABA which is 1
                    
                    k = nex[k]
            
            return nex 
        
        if len(needle) == 0 and len(haystack) == 0:
            return 0 
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        nex = findNext(needle)
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
           
            else:
                j = nex[j]

               
        
        if j < len(needle):
            return -1 
        else:
            return i-len(needle)

                

if __name__ == "__main__":
    haystack = "hello"
    needle = "ABDABCKEABDABDF"
    print(Solution().strStr(haystack, needle))