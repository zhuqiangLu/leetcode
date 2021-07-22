class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0 
        
        offset = {}
        n_l = len(needle)

        for i in range(n_l):
            offset[needle[i]] = n_l - i 

        dic = {
            needle:True
        }


        i, j, h_l = 0, 0, len(haystack)

        while i <= h_l - n_l:
            j = 0
            if dic.get(haystack[i:i+n_l]):
                return i

            if i + n_l == h_l:
                return -1

            if haystack[i + n_l] in offset:
                i += offset[haystack[i + n_l]]
            else:
                i += n_l + 1

        return -1
                

if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(Solution().strStr(haystack, needle))