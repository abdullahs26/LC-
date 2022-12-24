# Recursive soln
class Solution(object):
    def depthSum(self, nestedList):
        sum = dfs(nestedList, 1)
        return sum

    def dfs(self, nestedlist, depth):
        sum = 0
        if (len(nestedlist == 0)):
            return 0
        for item in nestedlist:
            if item.isInteger():
                sum += depth*item.getInteger()
            else:
                sum+=self.dfs(item.getList(), depth+1)
        return sum