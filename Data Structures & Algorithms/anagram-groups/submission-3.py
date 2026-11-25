class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []
        anagramMap = {}

        for string in strs:
            sortedStr = "".join(sorted(string))
            if sortedStr in anagramMap:
                anagramMap[sortedStr].append(string)
            else:
                anagramMap[sortedStr] = [string]

        for key in anagramMap:
            output.append(anagramMap[key])

        return output