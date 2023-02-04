class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashmap = {}
        count = 0

        for i in nums:
            if i in hashmap:
                count += hashmap[i]
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        return count