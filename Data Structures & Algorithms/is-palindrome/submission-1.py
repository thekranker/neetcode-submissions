class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # pointers O(1) space
        left = 0
        right = len(s) - 1

        # convert the string to all lower case O(n)
        s = s.lower()

        while left < right:
            
            # left is non-alphanum
            if not s[left].isalnum():
                left += 1
                continue
            
            # right is non-alphanum
            if not s[right].isalnum():
                right -= 1
                continue

            if s[right] != s[left]:
                return False

            left += 1
            right -= 1

        return True
            

            


