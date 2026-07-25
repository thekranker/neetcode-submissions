class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # - Brainstorming -
        # My initial idea is to brute force this in some way.
        # The main goal here is to find the greatest positive difference between two
        # numbers in the prices array.
        # This can be done in O(n^2) by comparing all the numbers and finding the greatest
        # difference between them (brute force).
        # Im challenged to complete this in O(n) and space complexity O(1).
        # Im thinking of an idea where the array is looped through once and the difference
        # betwen the first number and any number is stored, so that the difference between
        # other numbers could be calculated, but I believe this would still be O(n^2) and
        # would be a more complicated implementation.
        # The hints are suggesting that we treat i as a selling value and find the minimum
        # buy value to the left of i. This makes sense to me but I feel like this would still
        # be O(n^2) complexity. 


        # - Plan -
        # 1.) Create variables
        #     - lowestVal (lowest value to the left of index)
        #     - greatestDifference (stores the greatest current positive difference)
        # 2.) Iterate through the entire array
        # 2a.) Treat the value at index as the selling point and comparing it to the 
        #      greatestDifference
        # 2b.) Then compare the lowestVal and the current val and see if it needs updating
        # 3.) Return the greatestDifference identified O(n) TC & O(1) SC


        # step 1
        lowestVal = prices[0]   # initial price
        greatestDifference = 0  # minimum profit that can be made

        # step 2
        for price in prices:
            # step 2a
            if price - lowestVal > greatestDifference:
                greatestDifference = price - lowestVal
            # step 2b
            if lowestVal > price:
                lowestVal = price
        
        # step 3
        return greatestDifference

            









