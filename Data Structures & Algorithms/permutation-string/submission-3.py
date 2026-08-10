class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hashMap = {}

        # populate the characters and frequency of s1 to check for permutation
        for char in s1:
            hashMap[char] = hashMap.get(char, 0) + 1


        # pointers (sliding window)
        left = 0
        right = 0

        # curr window map, return true if the two maps match
        currMap = {}


        while right in range(len(s2)):
            
            # add to the window
            if s2[right] in hashMap:
                currMap[s2[right]] = currMap.get(s2[right], 0) + 1
                right += 1
                
                # check if window is too large
                if right - left > len(s1):
                    # remove left val from currMap
                    if s2[left] in currMap:
                        currMap[s2[left]] -= 1
                    left += 1

                # check if permutation match
                if currMap == hashMap:
                    return True


            # move the window by one
            else:
                if s2[left] in currMap:
                    currMap[s2[left]] -= 1
                left += 1
                right += 1


        return False
        
        
