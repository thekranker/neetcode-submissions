class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Plan
        # 1.) Go through each string in strs
        # 2.) Sort each string & check to see if the key already exists in a map
        # 3.) If it does exist, append the string to the values list of that key;
        #     if it doesn't exist, create a new key : value pair
        # 4.) Repeat until all the anagrams are detected, then return them


        anagram_map = {}
        groupedAnagrams = []

        # Step 1 / Step 4
        for string in strs:
            
            # Step 2
            if "".join(sorted(string)) in anagram_map:
                # Step 3 (part 1)
                anagram_map["".join(sorted(string))].append(string)
            else:
                # Step 3 (part 2)
                anagram_map["".join(sorted(string))] = [string]


        # Step 4 (part 2)
        for key in anagram_map:
            groupedAnagrams.append(anagram_map[key])

        return groupedAnagrams





            