class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        def recurFunc(candidates: List[int], target: int) -> List[List[int]]:

            results = []

            # base case
            if not candidates:
                return []

            if candidates[0] == target:
                results.append([candidates[0]])

            # including
            if candidates[0] < target:
                lists = recurFunc(candidates[1:], target - candidates[0])
                for list in lists:
                    list.append(candidates[0])
                results.extend(lists)
            
            # not including

            i = 1
            while i < len(candidates) and candidates[0] == candidates[i]:
                i += 1
            results.extend(recurFunc(candidates[i:], target))

            return results
        

        return recurFunc(candidates, target)

