class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        # x y z z x y
        # z x y z a b c

        map = {}

        left = 0
        longestSubstring = 0
        for index, char in enumerate(s):
            if not char in map or map[char] < left:
                map[char] = index
                currSubstring = index - left + 1
                if currSubstring > longestSubstring:
                    longestSubstring = currSubstring
            else:
                left = map[char] + 1
                map[char] = index
        
        return longestSubstring

        # thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert
        # 

            