class Solution:
    def isValid(self, s: str) -> bool:

        def isOpenBracket(char: str) -> bool:
            return char in '{(['

        def isClosedBracket(char: str) -> bool:
            return char in '})]'

        def isMatchingBracket(char: str) -> str:
            if char == '}':
                return '{'
            if char == ')':
                return '('
            if char == ']':
                return '['


        stack = []

        for c in s:
            print(c)

            if isOpenBracket(c):
                stack.append(c)
            
            elif isClosedBracket(c) and not stack:
                return False

            elif isClosedBracket(c) and isMatchingBracket(c) == stack[-1]:
                stack.pop()
            else:
                return False


        if len(stack) == 0:
            return True
        
        return False