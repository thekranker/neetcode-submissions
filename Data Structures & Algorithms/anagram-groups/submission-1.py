from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        hashMap = defaultdict(list)

        for string in strs:
            arr = [0] * 26
            for char in string:
                arr[ord(char) - ord('a')] += 1
            hashMap[tuple(arr)].append(string)

        for strs in hashMap:
            output.append(hashMap[strs])

        return output
            