from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        hashMap = defaultdict(list)

        for string in strs:
            sortedStr = sorted(string)
            hashMap[tuple(sortedStr)].append(string)

        for strs in hashMap:
            output.append(hashMap[strs])

        return output
            