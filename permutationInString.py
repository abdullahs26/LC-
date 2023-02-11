class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        l = 0

        for i in range(len(s1)):
            s1Count[ord("a") - ord(s1[i])] += 1
            s2Count[ord("a") - ord(s2[i])] += 1

        for r in range(len(s1), len(s2)):
            if s1Count == s2Count:
                return True

            s2Count[ord("a") - ord(s2[r])] += 1
            s2Count[ord("a") - ord(s2[l])] -= 1
            l += 1

        return s1Count == s2Count