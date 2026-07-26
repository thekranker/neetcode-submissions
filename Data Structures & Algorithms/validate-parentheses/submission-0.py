class Solution:

    def isClosingBracket(self, s: str):
       return s in "})]"

    def isOpeningBracket(self, s: str):
       return s in "{(["


    def isMatchingBrackets(self, s1: str, s2: str):
        if s1 == "[" and s2 == "]": return True
        if s1 == "{" and s2 == "}": return True
        if s1 == "(" and s2 == ")": return True
        return False

    def isValid(self, s: str) -> bool:
        
        # - Brainstorming -
        # I'm challenged to complete this in O(n) TC & O(n) SC
        # Using hint 2, we could use a stack for storing brackets and making sure they match
        # This would require a few different methods, one to compare to see if brackets match
        # Another would be a stack structure that defines what the stack would be.


        stack = []

        for char in s:
            if self.isOpeningBracket(char):
                stack.append(char)
            if self.isClosingBracket(char):
                if not stack:
                    return False
                if not self.isMatchingBrackets(stack.pop(), char):
                    return False
        
        return not stack
                
















