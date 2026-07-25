class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # - Brainstorming -
        # I need to remember to be case-insensitive and ignore all alpha-numeric
        # characters.
        # My initial thought for this is a like .toLowerCase method or something of
        # the sort.
        # For the characters, I'd probably use ASCII numbers to confirm they are
        # alphanumeric or not.
        # Googled the .lower method to be case-insensitive, confirmed.
        # Googled the .isalnum() string method to check whether a number is alpha numeric.
        # "? racecar ?"


        # - Plan -
        # 1.) Iterate through the string backwards
        # 2.) Use a forwardIndex to check where I am in the string in order to account
        #     for non-alphanumeric characters. 
        # 3.) Always skip non-alphanumeric characters by increasing the index & re-compare
        # 4.) If the comparison ever fails, return false, else return true


        forwardIndex = 0
        backwardIndex = len(s) - 1
        while forwardIndex < len(s) and backwardIndex >= 0:

            if not s[forwardIndex].isalnum():
                forwardIndex += 1
                continue
            
            if not s[backwardIndex].isalnum():
                backwardIndex -= 1
                continue
            
            if s[forwardIndex].lower() != s[backwardIndex].lower():
                return False

            forwardIndex += 1
            backwardIndex -= 1

        return True








