from typing import List

class Solution:
    def fullJustify (self, words: List[str], maxWidth: int) -> List[int]:
        res = list()
        line = list()
        lineLen = 0


        def makeLastLine(line, maxWidth, lineLen):
            if len(line) != 0:
                out = list()
                for word in line:
                    out.append(word)
                    out.append(" ")
                # remove the last space
                out.pop(-1)
                last = [" " for _ in range(maxWidth-(lineLen))]
                out.append("".join(last))
            
            return "".join(out)
    
        def makeLine(line, maxWidth, lineLen):
            # num of space =  #word - 1
            spaces = [" " for _ in range(len(line)-1)]
            
            carry = maxWidth - lineLen
            for i in range(len(spaces)):

                carry -= 1
                if carry < 0:
                    break
                spaces[i] += " "
            i = 0
            print(line, spaces, lineLen, carry)
            while carry > 0:
            
                spaces[i] += " "
                carry -= 1
                i += 1
                if i >= len(spaces):
                    i = 0
            # merge spaces and words 
            out = list()
            for i in range(len(line)-1):
                
                out.append(line[i])
                out.append(spaces[i])
            out.append(line[-1])

            return "".join(out)

        # select word for a line
        for word in words:
            if lineLen + len(word) > maxWidth:
                if len(line) == 1:
                    res.append(makeLastLine(line, maxWidth, lineLen-1))
                else:
                    res.append(makeLine(line, maxWidth, lineLen-1))
                lineLen = len(word) + 1
                line = [word]
            else:
                # 1 for space
                lineLen += len(word) + 1
                line.append(word)
        
        if len(line) != 0:
            res.append(makeLastLine(line, maxWidth, lineLen-1))
            
        
        for r in res:
            print(len(r))


        return res


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    # words = ["What","must","be","acknowledgment","shall","be"]
    #words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]

    maxWidth = 16
    print(Solution().fullJustify(words, maxWidth))