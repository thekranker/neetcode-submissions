class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def isOperator(string: str):
            return string in "+-*/"
        
        # define result int
        result = 0

        # implement a stack
        rpnStack = []

        # base case check
        if len(tokens) == 1:
            return int(tokens[0])
        
        # loop through tokens, push each value to stack
        # if the value is not alpha-numeric, treat it as an operator
        for token in tokens:
            if isOperator(token):
                operator = token
                a = int(rpnStack.pop())
                b = int(rpnStack.pop())
                if token == "+":
                    result = a + b
                    rpnStack.append(result)
                elif token == "-":
                    result = b - a
                    rpnStack.append(result)
                elif token == "*":
                    result =  a * b
                    rpnStack.append(result)
                elif token == "/":
                    result = int (b/a)
                    rpnStack.append(result)
            else:
                rpnStack.append(token)


        # return result
        return result
    