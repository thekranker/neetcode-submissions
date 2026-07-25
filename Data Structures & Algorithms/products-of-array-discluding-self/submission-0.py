class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #  - Brainstorming -
        # I need to create a system where each number in an array becomes the product
        # of all other numbers in the array except itself.
        # This could be done in O(n^2) time by going through the array for each number
        # in the array (brute force).
        # I've been challenged to solve it in O(n) time without using division
        # What if I tried an approach where I stored values that have already been
        # accessed / accounted for.
        # Idea - I'm going through the arr from left to right and then right to left.
        # Im going to create a new array for each iteration 'left' and 'right' and
        # its going to be multiplicative, so each one multiplies on the other.
        # When finding the value of a certain index, we would have to multiply the right
        # and the left sides of it to get the right number.


        # - Plan -
        # 1.) Loop through the array from left to right, storing the multiplied values
        #     as we progress (part 1), then do it from right to left (part 2)
        # 2.) Loop through a result array of size 'len(nums)' and put in the values for
        #     each spot in the array
        # 3.) Return the result array


        left_arr = [1] * len(nums)
        right_arr = [1] * len(nums)
        result = [1] * len(nums)

        # step 1 (part 1)
        for i in range(0, len(nums), 1):
            if (i != 0):
                left_arr[i] = left_arr[i-1] * nums[i-1]
            else:
                left_arr[i] = 1
        # step 1 (part 2)
        for i in range(len(nums) - 1, -1, -1):
            if (i != len(nums) - 1):
                right_arr[i] = right_arr[i+1] * nums[i+1]
            else:
                right_arr[i] = 1

        # step 2
        for i in range(0, len(nums), 1):
            result[i] = left_arr[i] * right_arr[i]
        
        # step 3
        return result
        


        