class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        f = 0

        while True:
            s = nums[s]
            f = nums[nums[f]]

            if s == f:
                break
        
        s2 = 0

        while True:
            s = nums[s]
            s2 = nums[s2]

            if s == s2:
                return s