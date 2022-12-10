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
                # Check if top of stack is a closing bracket and stack is not empty.
                if stack and stack[-1] == closeToOpen[n]:
                    stack.pop()
                # If stack does not matching closing bracket, return False
                else:
                    return False
            else:
                stack.append(n)
        
        if stack:
            return False
        else:
            return True