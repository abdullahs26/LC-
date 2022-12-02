class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        # Maps values in nums to their freqency.
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Populates freq array, where index maps to list of 
        # numbers that occur that many times in nums.
        for n, c in count.items():
            freq[c].append(n)
        
        # Iterate through freq array to find top K elements.
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
