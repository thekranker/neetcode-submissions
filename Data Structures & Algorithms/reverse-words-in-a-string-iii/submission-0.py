class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverseString(s2: str) -> str:

            left = 0
            right = len(s2) - 1
            temp = []
            
            for c in s2:
                temp.append(c)

            while left < right:
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1

            return "".join(temp)

        output = ""

        left = 0
        right = 0
        while right < len(s):
            while right < len(s) and s[right] != ' ':
                right += 1
            output += reverseString(s[left:right])

            if right < len(s) and s[right] == ' ':
                output +=  ' '
            right += 1
            left = right

        return output

        






