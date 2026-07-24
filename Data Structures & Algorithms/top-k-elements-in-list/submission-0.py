class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Brainstorming
        # i need to find a way to actively store the top k most frequent elements
        # one idea i have is to brute force it and count every element O(n^2)
        # i could try a hash map, go through the array once and increment the keys if-
        # they match and return the top 2 from the hash map. this would be a time complex-
        # of O(n + n) -> O(n)
        # the question now is how to return the top 2
        # this could be done by looping through the map once and storing the two values and-
        # comparing and maintaing the top 2 values
        # i need to revisit my approach to getting the top 2 values -> need better efficiency
        # revise by using bucket sort


        # Plan
        # 1.) Create a hash map & bucket_sort array
        # 2.) Iterate through every element in nums. If it exists already, increment it for the
        #     key in the hash map, else add a new key and store it as 1
        # 3.) Iterate through the map, place them in a bucket sort array, picking the top 2

        nums_map = defaultdict(int)
        bucket_sort = [[] for _ in range(len(nums) + 1)]
        k_frequent = []

        for num in nums:
            nums_map[num] += 1
    
        for key in nums_map:
            bucket_sort[nums_map[key]].append(key)

        index = len(nums)
        while len(k_frequent) < k and index >= 0:
            if bucket_sort[index] != []:
                k_frequent.extend(bucket_sort[index])
            index -= 1

        return k_frequent

        

            

