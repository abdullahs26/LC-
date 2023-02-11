class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        startIdx = 0
        result = sys.maxsize
        currSum = 0
        lowestWindowSize = 0

        for i in range(0, len(nums)):
            currSum += nums[i]
            while currSum >= target:
                result = min(result, i - startIdx + 1)
                currSum -= nums[startIdx]
                startIdx += 1
        
        if result == sys.maxsize:
            return 0
        else:
            return result