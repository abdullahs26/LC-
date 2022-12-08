class Solution:     
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            # use count as a hashmap to track the number of times a letter occurs.
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            # store all strings with the same count hashmap in dict
            anagrams[tuple(count)].append(s)
        
        return anagrams.values()