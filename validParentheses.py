class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for n in s:
            if n in closeToOpen:
                if stack and stack[-1] == closeToOpen[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        
        if stack:
            return False
        else:
            return True