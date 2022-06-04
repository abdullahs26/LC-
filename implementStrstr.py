class Solution:
    def strStr(self, haystack, needle):
        
        if not needle:
            return 0
        
        else:
            start = 0
            end = len(needle)
            
            while end <= len(haystack):
                
                if haystack[start: end] == needle:
                    return start
                
                else:
                    start += 1
                    end = (start + len(needle))
                    
            return -1