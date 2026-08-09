class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # variables
        res = 0
        currMostFreq = 0

        # pointers
        l = 0

        # map
        freqMap = {}

        for r in range(len(s)):

            # increment val in freqMap
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1

            # find the current most frequent
            currMostFreq = max(freqMap[s[r]], currMostFreq)

            # check validity
            while (r - l + 1) - currMostFreq > k:
                freqMap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

