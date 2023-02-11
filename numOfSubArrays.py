class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        # Get sum of initial window of size k
        fSum = sum(arr[:k])
        avg = 0
        counter = 0
        avg = fSum / k
        # Check if initial window has avg greather than or equal to threshold
        if avg >= threshold:
            counter += 1

        for i in range(k, len(arr)):
            # Move window
            fSum -= arr[i - k]
            fSum += arr[i]
            # Caculate new avg and check if it is greather than or equal to threshold
            avg = fSum / k
            if avg >= threshold:
                counter += 1
                
        return counter