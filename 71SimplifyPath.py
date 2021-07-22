class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = list()

        i = 0
        while i < len(path):
            if path[i] == "/":
                # find next slash 
                j = i + 1
                while j < len(path):
                    if path[j] == '/':
                        break 
                    else:
                        j += 1
                
                name = path[i:j]
                i = j
                # print(name, stack)
                if name == '/..':
                    if len(stack) > 0:
                        stack.pop(-1)
                    
                
                elif len(name) != 1 and name != "/.":
                    stack.append(name)
                    
        
        if len(stack) == 0:
            stack.append('/')

        return "".join(stack)
            
if __name__ == "__main__":
    path = "/a/./b/../../c/"
    path = "/home//foo/"
    path = "/../"
    path = "/home/"
    print(Solution().simplifyPath(path))