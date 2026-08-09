class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        # result
        longestCount = 0
        
        # character frequency map
        freqMap = {}
        mostFreqVal = 0

        # pointers
        left = 0
        right = 0

        # slide the window through the string 's'
        while right in range(len(s)):

            currVal = s[right]

            # add to freqMap
            if currVal not in freqMap:
                freqMap[currVal] = 1
            else:
                freqMap[currVal] += 1

            # compare most frequent characters
            if freqMap[currVal] > mostFreqVal:
                mostFreqVal = freqMap[currVal]
                mostFreqChar = currVal
            
            if mostFreqVal + k >= right - left + 1:
                longestCount = max(longestCount, right - left + 1)

            while mostFreqVal + k < right - left + 1:
                freqMap[s[left]] -= 1
                left += 1
            right += 1


        return longestCount
            

        

        

        
        