class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        temp = [i for i in s if i.isalpha()][::-1]
        
        result = ""
        index = 0
        
        for i in range(len(s)):
            if s[i].isalpha():
                result += temp[index]
                index +=1
            else:
                result += s[i]
                
        return result