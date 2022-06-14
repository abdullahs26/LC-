class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        onlyLetters = []
        nonLetters = [None] * len(s)
        idx = 0
        for i in s:
            if i.isalpha() == True:
                onlyLetters.append(i)
            else:
                nonLetters[idx] = i
            idx += 1
        
        idx = 0
        string = ""
        
        for i in onlyLetters[::-1]:
            for j in nonLetters:
                if (nonLetters[idx] != None):
                    string += nonLetters[idx]
                    idx += 1
            string += i
            idx += 1
    
        for i in nonLetters:
            if (idx >= len(nonLetters)):
                break
            else:
                if (nonLetters[idx] != None):
                    string += nonLetters[idx]
                    idx += 1
        return string