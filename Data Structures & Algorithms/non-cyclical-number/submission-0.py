class Solution:
    def isHappy(self, n: int) -> bool:

        seenNums = set()
        currNum = n

        while currNum != 1:

            if currNum in seenNums:
                return False

            seenNums.add(currNum)

            temp = 0
            for digit in str(currNum):
                temp += int(digit) * int(digit)
            currNum = temp 


        return True
        